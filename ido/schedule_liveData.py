#-*- coding: utf-8 -*-
import os
import django
import datetime

import sys

path = '/home/cxz3619/ipark_django/'
sys.path.append(path)
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)) + '/ipark_django')))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "firstProject.settings")
django.setup()
from ido.models import liveData

now = datetime.datetime.now() - datetime.timedelta(hours=3)
nowDatetime = now.strftime('%Y/%m/%d %H:%M:%S')
liveData.objects.filter(enter_time__lt=nowDatetime).delete()