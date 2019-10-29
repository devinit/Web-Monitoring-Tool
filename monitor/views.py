from django.http import HttpResponse
from .utils import parse_log
from django.views.decorators.csrf import csrf_exempt
# TODO: from future import do_something


@csrf_exempt
def receive_data(request):
    if request.method == "POST":
        text_data = request.POST.get('data', None)
        if text_data:
            json_data = parse_log(text_data)
            return HttpResponse(status=202)
            # return HttpResponse(json.dumps(json_data), status=202)
            # TODO: do_something(json_data)
    return HttpResponse(status=405)
