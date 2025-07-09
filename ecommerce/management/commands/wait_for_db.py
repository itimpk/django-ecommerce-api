# ecommerce_api/management/commands/wait_for_db.py
import time
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from django.db import connections # <-- Ensure this import is there

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_conn = connections['default'] # Get the default database connection object
        db_up = False
        while db_up is False:
            try:
                # Attempt to open a cursor to force a real connection check
                with db_conn.cursor() as cursor:
                    cursor.execute("SELECT 1") # A simple query to test connection
                db_up = True
            except (Psycopg2Error, OperationalError) as e:
                self.stdout.write(f'Database unavailable ({e}), waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))