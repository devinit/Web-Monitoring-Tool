from django.contrib import admin
from monitor.models import (
    Server,
    Domain,
    Status,
    Task,
    StatusUpdate,
    Alert,
    Watcher,
    Settings
)


class ServerAdmin(admin.ModelAdmin):
    list_display = ['provider', 'description', 'ip']
    save_on_top = True


class DomainAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'url', 'server__ip']
    save_on_top = True


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name', 'colour']
    save_on_top = True


class TaskAdmin(admin.ModelAdmin):
    list_display = ['server__ip', 'name', 'description', 'status', 'show_on_dashboard']
    save_on_top = True


class StatusUpdateAdmin(admin.ModelAdmin):
    list_display = ['status__name', 'task__name']
    save_on_top = True


class AlertAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'message', 'platform']
    save_on_top = True


class WatcherAdmin(admin.ModelAdmin):
    list_display = ['description', 'task__name', 'watch_status__name', 'switch_status__name', 'duration', 'alert__name']
    save_on_top = True


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['task__name', 'key', 'value']
    save_on_top = True


admin.site.register(Server, ServerAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(StatusUpdate, StatusUpdateAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Watcher, WatcherAdmin)
admin.site.register(Settings, SettingsAdmin)
