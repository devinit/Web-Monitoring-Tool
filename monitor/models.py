"""
    Database Models
"""
from django.contrib.auth.models import User
from django.db import models

from datetime import datetime
import operator

from .utils import json_len, json_in


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

    def available_methods(self):
        return [
            'timestamp_uptodate',
            'free_memory'
        ]

    def available_operators(self):
        return [
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
                return json_len
            elif operator_name == "in":
                return json_in
        return None

    def timestamp_uptodate(self, _,  _, expected_value):
        timestamp = self.records().filter(key='time_stamp').first().value
        then = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        now = datetime.now()
        if now - then > datetime.timedelta(minutes=int(expected_value)):
            return False
        return True

    def free_memory_percent(self, _, operator_name, expected_value):
        free_memory = float(self.records().filter(key='mem_free').first().value)
        total_memory = float(self.records().filter(key='mem_total').first().value)
        memory_percent = (free_memory/total_memory) * 100
        op_func = self.get_operator(operator_name)
        return op_func(memory_percent, float(expected_value))

    def pid(self, method_arg, operator_name, expected_value):
        pid_record = self.records().filter(key='{}_pid'.format(method_arg)).first().value
        op_func = self.get_operator(operator_name)
        if operator_name != "in":
            try:
                expected_value = float(expected_value)
            except ValueError:
                pass
        return op_func(pid_record, expected_value)

    def docker_id(self, _, operator_name, expected_value):
        did_record = self.records().filter(key='docker_ids').first().value
        op_func = self.get_operator(operator_name)
        if operator_name != "in":
            try:
                expected_value = float(expected_value)
            except ValueError:
                pass
        return op_func(did_record, expected_value)


class Domain(BaseEntity):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=255)
    server = models.ForeignKey('Server', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Status(models.Model):
    name = models.TextField(blank=True, null=True)
    colour = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "statuses"


class Task(BaseEntity):
    server = models.ForeignKey('Server', on_delete=models.CASCADE)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    show_on_dashboard = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StatusUpdate(BaseEntity):
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)

    def __str__(self):
        return "{} -> {}".format(self.status, self.task)


class Alert(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    platform = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Watcher(models.Model):
    description = models.TextField(blank=True, null=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    watch_status = models.ForeignKey(
        'Status',
        related_name='watch_status',
        on_delete=models.CASCADE
    )
    switch_status = models.ForeignKey(
        'Status',
        related_name='switch_status',
        on_delete=models.CASCADE
    )
    duration = models.IntegerField(default=5)
    alert = models.ForeignKey('Alert', on_delete=models.CASCADE)

    def __str__(self):
        return "{} watcher for {}".format(self.watch_status, self.task)


class Settings(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{}: {}".format(self.key, self.value)

    class Meta:
        verbose_name_plural = "settings"


class Record(BaseEntity):
    server = models.ForeignKey('Server', on_delete=models.CASCADE, blank=True, null=True)
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return "{} ({}: {})".format(self.server, self.key, self.value)