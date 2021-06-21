from .models import liveData,memberData,historicalRecord,covidRecord
from django_cron import CronJobBase,Schedule
import datetime
import logging

logger = logging.getLogger("mylogger")



def delete_livedata():
    
    logger.info("hi")
    print("hi") 
    