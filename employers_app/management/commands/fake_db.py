from django.core.management.base import BaseCommand
from employers_app.tests.utils import create_employers


class Command(BaseCommand):
    """creates fake db for developers
        new users -> 50
        new employers -> 50

    Args:
        BaseCommand: python manage.py fake_db
    """

    def handle(self, *args, **options):
        create_employers(count=50)
