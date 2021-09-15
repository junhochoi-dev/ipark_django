#!/usr/bin/env python3.6
import os
import django
import datetime

import sys

path = '/home/cxz3619/ipark_django'
sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstProject.settings")
django.setup()
from ido.models import liveData,memberData,historicalRecord,covidRecord

now = datetime.datetime.now() - datetime.timedelta(days=1)
nowDatetime = now.strftime('%Y/%m/%d %H:%M:%S')
covidRecord.objects.filter(enter_time__lt=nowDatetime).delete()