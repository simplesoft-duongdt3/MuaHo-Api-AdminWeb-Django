from django.http import HttpResponse
import json
from datetime import date, datetime

def obj_to_dict(obj):

    if isinstance(obj, (datetime)):
        return '{:%Y-%m-%d %H:%M:%S}'.format(obj)
    if isinstance(obj, (date)):
        return '{:%Y-%m-%d}'.format(obj)
    return obj.__dict__

def toJson(obj):
    return json.dumps(obj=obj, default=obj_to_dict, ensure_ascii=False).encode('utf8')

def responseJson(obj):
    return HttpResponse(toJson(obj), content_type="application/json")