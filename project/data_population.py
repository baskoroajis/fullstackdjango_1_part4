# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

import django
django.setup()

from apptwo.models import User
from faker import Faker

fakegenerator = Faker()

def populate_user_data(N= 10):
    for entry in range(N):
        first_name = fakegenerator.first_name()
        last_name = fakegenerator.last_name()
        email = fakegenerator.email()
        t = User.objects.get_or_create(first_name=first_name,last_name=last_name,email=email)[0]
        # dataUser.save()
        t.save()
        print('first name', first_name)
        print('last name', last_name)
        print('email ', email)


if __name__ == '__main__':
    populate_user_data(10)
