from django.core.management.base import BaseCommand
from employers_app.tests.utils import create_user


class Command(BaseCommand):
    """creates fake db for developers
        new users -> 50
    Args:
        BaseCommand: python manage.py fake_db
    """

    def handle(self, *args, **options):
        create_user(count=50)

