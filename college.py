import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "technexUser.settings")
application = get_wsgi_application()
# import django
# django.setup()
import csv
from Auth.models import College

with open('ca_college.csv','rb') as f:
    data = csv.reader(f)
    for row in data:
        College.objects.create(collegeName=row[0],status=True)
        print row[0]
