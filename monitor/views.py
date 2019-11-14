import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth.decorators import login_required

from .utils import parse_log, get_client_ip
from .models import Server, Record, Domain


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


@login_required
def dashboard(request):
    return render_to_response('monitor/index.html', {})

@login_required
def settings(request):
    return render_to_response('monitor/index.html', {})

@csrf_exempt
def servers(request):
    servers = Server.objects.all()
    result = []
    for server in servers:
        serv_obj = {}
        serv_obj["id"] = server.pk
        serv_obj["ip"] = server.ip
        serv_obj["description"] = server.description
        serv_obj["domains"] = []
        serv_domains = Domain.objects.filter(server=server)
        for serv_domain in serv_domains:
            serv_obj["domains"].append(serv_domain.url)
        result.append(serv_obj)
    return HttpResponse(json.dumps(result), content_type='application/json')


@csrf_exempt
def records(request):
    server_id = request.GET.get('server', None)
    key = request.GET.get('key', None)

    server = get_object_or_404(Server, pk=server_id)

    if key:
        qs = Record.objects.filter(server=server, key=key).order_by('created_on', 'key').values('key', 'value', 'created_on')
    else:
        qs = Record.objects.filter(server=server).order_by('created_on', 'key').values('key', 'value', 'created_on')

    return HttpResponse(json.dumps(list(qs), cls=DjangoJSONEncoder), content_type='application/json')


@csrf_exempt
def query(request):
    server_id = request.GET.get('server', None)
    query_name = request.GET.get('query', None)
    method_arg = request.GET.get('method_arg', None)

    server = get_object_or_404(Server, pk=server_id)

    if query_name in Server.available_queries:
        query_func = getattr(server, query_name)
        result = {"result": query_func(method_arg)}

        return HttpResponse(json.dumps(result, cls=DjangoJSONEncoder), content_type='application/json')
    return HttpResponse(status=500)
