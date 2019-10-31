import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response

from .utils import parse_log, get_client_ip
from .models import Server, Record


@csrf_exempt
def receive_data(request):
    if request.method == "POST":
        text_data = request.POST.get('data', None)
        if text_data:
            json_data = parse_log(text_data)
            server_ip = get_client_ip(request)
            server_obj, server_new = Server.objects.get_or_create(ip=server_ip)
            for key, value in json_data.items():
                new_record = Record(key=key, value=value, server=server_obj)
                new_record.save()
            return HttpResponse(json.dumps(json_data), status=202)
    return HttpResponse(status=405)


def dashboard(request):
    return render_to_response('monitor/dashboard.html', {})
