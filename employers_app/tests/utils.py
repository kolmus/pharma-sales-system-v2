from employers_app.models import Employee

from django.contrib.auth.models import User
from faker import Faker

faker = Faker("pl-PL")

def create_employee(count):
    users = []
    for i in range(count):
        profile = faker.simple_profile(),
        password = faker.password(length=12)
        user = User.objects.create_user(
            username=profile['username'],
            password=password, 
            first_name=profile['name'].split(" ")[0],
            last_name=profile['name'].split(" ")[1],
            email=profile['mail']
        )
        users.append({
            'object': user, 
            "username": profile['username'], 
            'password': password
        })
        if len(users) == 1:
            supervisor = Employee.objects.create(
                phone=faker.msisdn(),
                role=faker.job(),
                supervisor=None,
                user=user,
                is_active=faker.boolean(chance_of_getting_true=25),
                is_supervisor=faker.boolean(chance_of_getting_true=5)
            )
            users[0]['employer'] = supervisor
            
    for user in users[1:]:
        employee = Employee.objects.create(
            phone=faker.msisdn(),
            role=faker.job(),
            supervisor=supervisor,
            user=user,
            is_active=faker.boolean(chance_of_getting_true=25),
            is_supervisor=faker.boolean(chance_of_getting_true=5)
        )
        user['employer'] = employee
    print(users)