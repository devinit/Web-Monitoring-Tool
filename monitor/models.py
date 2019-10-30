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


class Domain(BaseEntity):
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=255)
    server = models.ForeignKey('Server', on_delete=models.CASCADE)


class Status(models.Model):
    name = models.TextField(blank=True, null=True)
    colour = models.TextField(blank=True, null=True)


class Task(BaseEntity):
    server = models.ForeignKey('Server', on_delete=models.CASCADE)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    show_on_dashboard = models.BooleanField(default=False)


class StatusUpdate(BaseEntity):
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)


class Alert(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    platform = models.TextField(blank=True, null=True)


class Watcher(models.Model):
    description = models.TextField(blank=True, null=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    watch_status = models.ForeignKey('Status', on_delete=models.CASCADE)
    switch_status = models.ForeignKey('Status', on_delete=models.CASCADE)
    duration = models.IntegerField(default=5)
    alert = models.ForeignKey('Alert', on_delete=models.CASCADE)


class Settings(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)
