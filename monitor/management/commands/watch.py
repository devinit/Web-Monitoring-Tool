"""Management command that fixes imported WP content."""

from django.core.management.base import BaseCommand

from monitor.models import Watcher


class Command(BaseCommand):
    """Management command that runs watchers."""

    help = 'Run watchers.'

    def handle(self, *args, **options):
        """Implement the command handler."""
        
        watchers = Watcher.objects.all()
        for watcher in watchers:
            watcher.watch()
