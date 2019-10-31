from django.contrib import admin
from monitor.models import (
    Server,
    Domain,
    Alert,
    Watcher,
    Record
)


class ServerAdmin(admin.ModelAdmin):
    list_display = ['provider', 'description', 'ip']
    save_on_top = True


class DomainAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'url', 'server']
    save_on_top = True


class AlertAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'message', 'platform']
    save_on_top = True


class WatcherAdmin(admin.ModelAdmin):
    list_display = ['description', 'method', 'expected_value', 'operator', 'alert']
    save_on_top = True


class RecordAdmin(admin.ModelAdmin):
    list_display = ['server', 'key', 'value', 'created_on']
    save_on_top = True


admin.site.register(Server, ServerAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Watcher, WatcherAdmin)
admin.site.register(Record, RecordAdmin)
