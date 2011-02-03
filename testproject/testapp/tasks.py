import datetime
from celery.decorators import task

from testapp.models import CeleryBeatLog

@task
def return_true():
    logger = return_true.get_logger()
    logger.info("Ran return_true at %s" % datetime.datetime.now().isoformat())    
    return True

@task
def log_timestamp():
    logger = log_timestamp.get_logger()
    logger.info("Ran log_timestamp at %s" % datetime.datetime.now().isoformat())
    return CeleryBeatLog.objects.create()
