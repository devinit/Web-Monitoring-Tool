"""
    Database Models
"""
from django.contrib.auth.models import User
from django.db import models


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
    method = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    expected_value = models.TextField(blank=True, null=True)
    alert = models.ForeignKey('Alert', on_delete=models.CASCADE)

    def __str__(self):
        return "{} watcher for {}".format(self.method, self.task)


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
