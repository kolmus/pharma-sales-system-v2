import pytest
from employers_app.tests.utils import create_fake_superuser, create_users

@pytest.fixture
def create_superuser_only():
    create_fake_superuser()