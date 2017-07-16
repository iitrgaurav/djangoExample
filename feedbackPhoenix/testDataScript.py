import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_phoenix_v0.settings')

import django
django.setup()

##FAKE POPULTE SCRIPT
import random
from feedback_app.models import userName, bfeedBack, mfeedBack
from faker import Faker

fakegen = Faker()
uname = ['John', 'arvil','germin', 'kitty']

def add_name():
    t = userName.objects.get_or_create(name=random.choice(uname))[0]
    t.save()
    return t

def populate(N=4):

    for entry in range(N):

        name = add_name()
        fakeText = fakegen.text()

        buddyfeedBack = bfeedBack.objects.get_or_create(buddyName=name,buddyResponse=fakeText)
        mentorfeedBack = mfeedBack.objects.get_or_create(mentorName=name,mentorResponse=fakeText)


if __name__ == '__main__':
    print('Populating Scripts!')
    populate(20)
    print('Populating complete!!')
