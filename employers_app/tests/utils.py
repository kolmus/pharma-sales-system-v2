from employers_app.models import Employee

from django.contrib.auth.models import User
from faker import Faker

faker = Faker("pl-PL")


def create_user() -> dict:
    """Creates fake user

    Returns:
        dict:
            id (int): id of new user in db
            username (str): username of new user
            password (str): password of new user
            obj (obj): new user object
    """
    profile = faker.simple_profile()
    password = faker.password(length=12)

    user_new = User.objects.create_user(
        username=profile["username"],
        password=password,
        first_name=profile["name"].split(" ")[0],
        last_name=profile["name"].split(" ")[1],
        email=profile["mail"],
    )
    return {"id": user_new.id, "username": profile["username"], "password": password, "obj": user_new}


def create_employers(count):
    """creates new count of fake Employee model objects

    Args:
        count (int): number of new employers

    Returns:
        list of dicts:
            id [int]: id of new user in db
            username [str]: username of new user
            password [str]: password of new user
            obj [obj]: new user object
    """
    employers = []
    for i in range(count):
        new_user_info = create_user()

        employee = Employee()
        employee.phone = faker.msisdn()
        employee.role = faker.job()
        if new_user_info["id"] == 1:
            employee.is_supervisor = True
        else:
            employee.supervisor = Employee.objects.get(id=1)
            employee.is_supervisor = False
        employee.user = new_user_info["obj"]
        employee.is_active = faker.boolean(chance_of_getting_true=75)
        employee.save()

        employers.append({"user_info": new_user_info, "employee": employee})
    return employers
