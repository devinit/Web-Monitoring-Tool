"""
    Database Models
"""
import json
from django.contrib.auth.models import User
from django.db import models

from datetime import datetime
import operator

from .utils import json_len_gte, json_in


class BaseEntity(models.Model):
    """An abstract model which allows all other models to inherit its characteristics.
    Gives every other model a field for the date it was created and the date it was updated."""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        abstract = True


class Server(BaseEntity):
    provider = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip = models.GenericIPAddressField()

    def __str__(self):
        return self.ip

    def records(self):
        return Record.objects.filter(server=self).order_by('-created_on')

    available_queries = [
        'query_timestamp_uptodate',
        'query_free_memory_percent',
        'query_pid',
        'query_docker_id',
        'query_generic'
    ]

    available_methods = [
        'timestamp_uptodate',
        'free_memory_percent',
        'pid',
        'docker_id',
        'generic'
    ]

    available_operators = [
        'lt',
        'le',
        'eq',
        'ne',
        'ge',
        'gt',
        'len',
        'in',
    ]

    def get_operator(self, operator_name):
        try:
            return getattr(operator, operator_name)
        except AttributeError:
            if operator_name == "len":
                return json_len_gte
            elif operator_name == "in":
                return json_in
        return None

    def query_timestamp_uptodate(self, _):
        timestamp = self.records().filter(key='time_stamp').first().value
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S %z")

    def timestamp_uptodate(self, _method_arg,  _operator_name, expected_value):
        timestamp = self.records().filter(key='time_stamp').first().value
        then = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S %z")
        now = datetime.now()
        if now - then > datetime.timedelta(minutes=int(expected_value)):
            return False
        return True

    def query_free_memory_percent(self, _):
        free_memory = float(self.records().filter(key='mem_free').first().value)
        total_memory = float(self.records().filter(key='mem_total').first().value)
        memory_percent = (free_memory/total_memory) * 100
        return memory_percent

    def free_memory_percent(self, _, operator_name, expected_value):
        free_memory = float(self.records().filter(key='mem_free').first().value)
        total_memory = float(self.records().filter(key='mem_total').first().value)
        memory_percent = (free_memory/total_memory) * 100
        op_func = self.get_operator(operator_name)
        return op_func(memory_percent, float(expected_value))


    def query_pid(self, method_arg):
        pid_record = self.records().filter(key='{}_pid'.format(method_arg)).first().value
        return json.loads(pid_record.replace("'", '"'))

    def pid(self, method_arg, operator_name, expected_value):
        pid_record = self.records().filter(key='{}_pid'.format(method_arg)).first().value
        op_func = self.get_operator(operator_name)
        if operator_name != "in":
            try:
                expected_value = float(expected_value)
            except ValueError:
                pass
        return op_func(pid_record, expected_value)

    def query_docker_id(self, _):
        did_record = self.records().filter(key='docker_ids').first().value
        return json.loads(did_record.replace("'", '"'))

    def docker_id(self, _, operator_name, expected_value):
        did_record = self.records().filter(key='docker_ids').first().value
        op_func = self.get_operator(operator_name)
        if operator_name != "in":
            try:
                expected_value = float(expected_value)
            except ValueError:
                pass
        return op_func(did_record, expected_value)

    def query_generic(self, method_arg):
        record = self.records().filter(key='{}'.format(method_arg)).first().value
        return record

    def generic(self, method_arg, operator_name, expected_value):
        record = self.records().filter(key='{}'.format(method_arg)).first().value
        op_func = self.get_operator(operator_name)
        if operator_name != "in":
            try:
                expected_value = float(expected_value)
            except ValueError:
                pass
        return op_func(record, expected_value)


class Domain(BaseEntity):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=255)
    server = models.ForeignKey('Server', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Alert(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    platform = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


    def alert(self, watcher, server):
        # placeholder
        message = "{} watcher failed for server {}.".format(watcher.description, server)
        print(message)
        return message


class Watcher(models.Model):
    AVAILABLE_METHODS = [
        ('timestamp_uptodate', 'Server responding'),
        ('free_memory_percent', 'Free memory percent'),
        ('pid', 'Process ID'),
        ('docker_id', 'Docker ID'),
        ('generic', 'Generic')
    ]
    AVAILABLE_OPERATORS = [
        ('lt', 'Less than'),
        ('le', 'Less Than or Equal To'),
        ('eq', 'Equal To'),
        ('ne', 'Not Equal'),
        ('ge', 'Greater Than or Equal'),
        ('gt', 'Greater Than'),
        ('len', 'Length'),
        ('in', 'String In'),
    ]
    description = models.TextField(blank=True, null=True)
    method = models.CharField(blank=True, null=True, max_length=255, choices=AVAILABLE_METHODS)
    operator = models.CharField(blank=True, null=True, max_length=3, choices=AVAILABLE_OPERATORS)
    expected_value = models.TextField(blank=True, null=True)
    method_arg = models.TextField(blank=True, null=True)
    alert = models.ForeignKey('Alert', on_delete=models.CASCADE)
    servers = models.ManyToManyField(Server)

    def __str__(self):
        return self.description


    def watch(self):
        servers = self.servers.all()
        for server in servers:
            method_func = getattr(server, self.method)
            watch_result = method_func(self.method_arg, self.operator, self.expected_value)
            if not watch_result:
                self.alert.alert(self, server)


class Record(BaseEntity):
    server = models.ForeignKey('Server', on_delete=models.CASCADE, blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} ({}: {})".format(self.server, self.key, self.value)
