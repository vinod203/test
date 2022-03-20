import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','enrolment.settings')
import django
django.setup()
from register.models import Student
from faker import Faker

fakegen = Faker()

def populate(N=20):
    for entry in range(N):
        fake_sname = fakegen.name()
        fake_email = fakegen.email()
        # fake_mob = fakegen.phone_number()
        fake_addr = fakegen.address()

        student = Student.objects.get_or_create(sname = fake_sname,semail= fake_email,saddr=fake_addr)

if __name__ == '__main__':
    print('Populating data please waint....')
    populate(50)
    print('Population complete')