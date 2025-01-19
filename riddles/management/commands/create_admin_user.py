from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

from decouple import config

UserModel = get_user_model()

USERNAME = config("USERNAME")
PASSWORD = config("PASSWORD")
EMAIL = config("EMAIL")


class Command(BaseCommand):

    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument("--username", default=USERNAME)
        parser.add_argument("--email", default=EMAIL)
    
    def handle(self, *args, **options):
        
        username = options["username"]
        email = options["email"]
        password = PASSWORD

        if UserModel.objects.filter(username__iexact=username, email__iexact=email).exists():
            raise CommandError("User already exists.")
        
        UserModel.objects.create_superuser(username, email, password)
        self.stdout.write(self.style.SUCCESS("User create successfully"))