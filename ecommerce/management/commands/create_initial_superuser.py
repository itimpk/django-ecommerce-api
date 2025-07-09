import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if one does not exist, using environment variables.'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get credentials from environment variables, provide secure defaults for production
        # !! IMPORTANT: Change these default passwords to strong, random ones for actual production
        # or ensure these env vars are ALWAYS set in your deployment environment.
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
        # This is where the password comes from env var, default is very insecure!
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'aVeryInsecurePassword123') 

        if not User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f'Creating superuser "{username}"...'))
            try:
                User.objects.create_superuser(username=username, email=email, password=password)
                self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error creating superuser: {e}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" already exists. Skipping creation.'))