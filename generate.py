import django
from crudApp.models import *
from faker import Faker
from random import *
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudDemo.settings')


django.setup()

faker = Faker()


def generate(n):
    for i in range(n):
        fsno = randint(4, 1000)
        fsname = faker.name()
        fsclass = randint(1, 12)
        fsaddress = faker.city()
        stu_record = Student.objects.get_or_create(
            sno=fsno, sname=fsname, sclass=fsclass, saddress=fsaddress)


generate(20)
