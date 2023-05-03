import json
from django.http import JsonResponse


def api_home(request, *argx, **kwargs):
    body = request.body
    data = {}
    print(request.GET) # url query params
    print(request.POST)
    try:
        data = json.loads(body)
    except:
        pass
    # print(data.keys())
    # data['headers'] = request.headers
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
