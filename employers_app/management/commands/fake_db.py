from django.core.management.base import BaseCommand
from employers_app.tests.utils import create_fake_superuser, create_users


class Command(BaseCommand):
    """creates fake db for developers
        1 new superuser (l:a@a.pl p:adminadmin)
        new users -> 50
    Args:
        BaseCommand: python manage.py fake_db
    """

    def handle(self, *args, **options):

        create_fake_superuser()
        create_users(count=50)
