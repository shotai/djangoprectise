from django.shortcuts import render
from httptest2.testmodule import tasks
from httptest2.testmodule.forms import TestModuleForm, DisplayModuleForm
import time
import json

# Create your views here.
def display_all(request):
    if request.method == 'POST':
        form = DisplayModuleForm(request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            if choice == 'DB':
                result = tasks.get_delivery.delay()
                while not result.ready():
                    time.sleep(3)
                d = json.loads(result.result)
                lst = []
                for i in d:
                    lst.append(i['fields'])
            else:
                result = tasks.get_delivery_restapi.delay()
                while not result.ready():
                    time.sleep(3)
                lst = result.result
                # python serializer
                # d = json.loads(result.result)
                # lst = []
                # for i in d:
                #     lst.append(i['fields'])
            return render(request, 'testmodule/index.html', {'form': form, 'delivery_list': lst})
    else:
        form = DisplayModuleForm()
    return render(request, 'testmodule/index.html', {'form': form})


def insert_all(request):
    if request.method == 'POST':
        form = TestModuleForm(request.POST)
        if form.is_valid():
            insertnumber = form.cleaned_data['insertnumber']
            choice = form.cleaned_data['choice']
            if choice == 'DB':
                result = tasks.insert_delivery.delay(int(insertnumber))
            elif choice == 'BATCH':
                result = tasks.insert_delivery_restapi.delay(int(insertnumber))
            elif choice == 'ONE':
                result = tasks.insert_delivery_restapi_single.delay(int(insertnumber))
            print result.id
    else:
        form = TestModuleForm()
    return render(request, 'testmodule/inserttestmodel.html', {'form': form})
