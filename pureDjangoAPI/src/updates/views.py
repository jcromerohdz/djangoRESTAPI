import json

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from pure_django_api.mixins import JsonResponseMixin

from .models import Update
# Create your views here.

def json_example_view(request):
    """
    URI -- for a REST API
    GET -- Retrieve
    """
    data = {
        "count": 1000,
        "content": "Dome new content"
    }
    return JsonResponse(data)

class JsonCBV(View):
    def get(self, reques, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Dome new content"
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, reques, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Dome new content"
        }
        return self.render_to_json_response(data)

class SirializedView(View):
    def get(self, reques, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj,], fields=('user', 'content'))
        json_data = data
        return HttpResponse(json_data, content_type='application/json')

class SirializedListView(View):
    def get(self, reques, *args, **kwargs):
        qs = Update.objects.all()
        data = serialize("json", qs, fields=('user', 'content'))
        json_data = data
        return HttpResponse(json_data, content_type='application/json')
