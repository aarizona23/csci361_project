from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from MainApp.models import UserProfile  # Replace 'myapp' with your app name

class Command(BaseCommand):
    help = 'Create a new user with a hashed password'

    def handle(self, *args, **options):
        username = 'ari'
        raw_password = 'ari23'

        # Hash the password securely
        hashed_password = make_password(raw_password)

        # Create a new user profile with the hashed password
        UserProfile.objects.create(username=username, password=hashed_password)

        self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
