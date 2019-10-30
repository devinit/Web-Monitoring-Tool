import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .utils import parse_log
from .models import Record


@csrf_exempt
def receive_data(request):
    if request.method == "POST":
        text_data = request.POST.get('data', None)
        if text_data:
            json_data = parse_log(text_data)

            for key, value in json_data.items():
                new_set = Record(key=key, value=value)
                new_set.save()
            return HttpResponse(json.dumps(json_data), status=202)
    return HttpResponse(status=405)
