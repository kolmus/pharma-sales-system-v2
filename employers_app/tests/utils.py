from django.contrib.auth.hashers import make_password
from employers_app.models import User

from faker import Faker

from random import shuffle

faker = Faker("pl-PL")


def create_user(count) -> list:
    response = []
    supervisors = []

    for i in range(count):
        new_user = User()
        profile = faker.simple_profile()
        new_user.set_password(faker.password(length=12))
        new_user.phone = faker.msisdn()
        new_user.name = profile["name"]
        new_user.email = profile["mail"]
        new_user.role = faker.job()
        if (len(response) + 1) % 15 == 1:
            shuffle(supervisors)
            supervisors.append(len(response) + 1)
            new_user.is_supervisor = True
        else:
            shuffle(supervisors)
            new_user.supervisor = User.objects.get(id=(supervisors[0]))
            new_user.is_supervisor = False
        new_user.is_active = faker.boolean(chance_of_getting_true=75)

        new_user.save()
        response.append(new_user)
    return response
