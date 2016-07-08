from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from httptest2.testmodule.models import TestModule
from httptest2.testrestapi.serializers import TestDeliverySerializer
import json
from django.core import serializers

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def testdelivery_list(request):
    if request.method == 'GET':
        deliveries = TestModule.objects.all()
        serializer = TestDeliverySerializer(deliveries, many=True)
        return JSONResponse(serializer.data)
        # python serializer
        # data = serializers.serialize('json', deliveries)
        # return JSONResponse(data, status=201)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        d = json.loads(data)
        print type(d)
        if isinstance(d, list):
            serializer = TestDeliverySerializer(data=d, many=True)
        else:
            serializer = TestDeliverySerializer(data=d)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        else:
            print serializer.errors
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def testdelivery_single(request, delivery_id):
    try:
        delivery = TestModule.objects.get(testmodule_id=delivery_id)
    except TestModule.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TestDeliverySerializer(delivery)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TestDeliverySerializer(delivery, data = data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        delivery.delete()
        return HttpResponse(status=204)

