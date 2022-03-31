from django.contrib.auth.hashers import make_password
from employers_app.models import User

from faker import Faker
# from datetime import date, timedelta
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
        if (len(response)+1) % 15 == 1:
            shuffle(supervisors)
            supervisors.append(len(response)+1)
            new_user.is_supervisor = True
        else:
            shuffle(supervisors)
            new_user.supervisor = User.objects.get(id=(supervisors[0]))
            new_user.is_supervisor = False
        new_user.is_active = faker.boolean(chance_of_getting_true=75)
        
        new_user.save()
        response.append(new_user)
    return response
        
        
        
        
        
        
#     return {"id": user_new.id, "username": profile["username"], "password": password, "obj": user_new}


# def create_employers(count) -> list:
#     """creates new count of fake Employee model objects

#     Args:
#         count (int): number of new employers

#     Returns:
#         list of dicts:
#             id [int]: id of new user in db
#             username [str]: username of new user
#             password [str]: password of new user
#             obj [obj]: new user object
#     """
#     employers = []
#     for i in range(count):
#         new_user_info = create_user()

#         employee = Employee()
#         employee.phone = faker.msisdn()
#         employee.role = faker.job()
#         if new_user_info["id"] == 1:
#             employee.is_supervisor = True
#         else:
#             employee.supervisor = Employee.objects.get(id=1)
#             employee.is_supervisor = False
#         employee.user = new_user_info["obj"]
#         employee.is_active = faker.boolean(chance_of_getting_true=75)
#         employee.save()

#         employers.append({"user_info": new_user_info, "employee": employee})
#     return employers


# def create_calendar_visit(count) -> list:
#     """Creates count of fake visits in CalendarSupervisor model

#     Args:
#         count (int): number of ner visits

#     Returns:
#         list: new objects
#     """
#     visits = []
#     for i in range(count):
#         new_visit = CalendarSupervisor()
#         employee = Employee.objects.filter(is_supervisor=True).first()
#         team = Employee.objects.filter(supervisor=employee)
#         new_visit.owner = employee
#         new_visit.meeting_date = date.today() + timedelta(days=(-14 + i))
#         new_visit.employee = team[randint(0, team.count() - 1)]
#         new_visit.note = faker.sentence(nb_words=40)
#         new_visit.save()
#         visits.append(new_visit)
#     return visits
