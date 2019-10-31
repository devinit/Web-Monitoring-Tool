"""Management command that fixes imported WP content."""

import pytz
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand

from monitor.models import Record


class Command(BaseCommand):
    """Management command that deletes old records."""

    help = 'Delete old records.'

    def handle(self, *args, **options):
        """Implement the command handler."""

        last_week = pytz.utc.localize(datetime.now() - timedelta(days=7))
        old_records = Record.objects.filter(created_on__lte=last_week)
        old_records.delete()
