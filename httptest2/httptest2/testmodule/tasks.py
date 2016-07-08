
import random
from httptest2.taskapp.celery import app, logger
from models import TestModule
import requests
import json
from django.core import serializers

@app.task(bind=True)
def insert_delivery(self, number):
    for i in range(number):
        testmodule_id = random.randrange(10000, 20000)
        status = i%2 == 0
        d = TestModule(testmodule_id=testmodule_id, status=status)
        d.save()
    return True

@app.task(bind=True)
def insert_delivery_restapi(self, number):
    lst = []
    for i in range(number):
        testmodule_id = random.randrange(10000, 50000)
        status = i % 2 == 0
        delivery = {"testmodule_id":testmodule_id, "status":status}
        lst.append(delivery)
    r = requests.post("http://localhost:8000/testrestapi/", json=json.dumps(lst))
    return True

@app.task(bind=True)
def insert_delivery_restapi_single(self, number):
    for i in range(number):
        testmodule_id = random.randrange(10000, 50000)
        status = i % 2 == 0
        delivery = {"testmodule_id":testmodule_id, "status":status}
        r = requests.post("http://localhost:8000/testrestapi/", json=json.dumps(delivery))
    return True

@app.task(bind=True)
def get_delivery(self):
    data = serializers.serialize('json', TestModule.objects.all())
    return data

@app.task(bind=True)
def get_delivery_restapi(self):
    r = requests.get("http://localhost:8000/testrestapi/")
    return r.json()
