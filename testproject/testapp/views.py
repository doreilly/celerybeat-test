from datetime import datetime

from django.http import HttpResponse, Http404
from celery.exceptions import TimeoutError

from testapp.models import CeleryBeatLog
from testapp.tasks import return_true

def test_celery_response(request):
    status_code = 500
    try:
        if return_true.delay().get(timeout=5):
            status_code = 200
    except TimeoutError:
        status_code = 503
    return HttpResponse("Status Code: %d" % status_code,
        status=status_code, content_type='text/plain')

def seconds_since_last_celery_beat(request):
    try:
        log = CeleryBeatLog.objects.latest()
        timestamp = log.timestamp
    except CeleryBeatLog.DoesNotExist:
        raise Http404
    delta = datetime.now() - timestamp
    seconds = delta.days * 60 * 60 * 24 + delta.seconds
    return HttpResponse(str(seconds), content_type='text/plain')
