from django.conf.urls import url
from httptest2.testrestapi import views

urlpatterns = [
    url(r'^$', views.testdelivery_list),
    url(r'^(?P<delivery_id>[0-9]+)/$', views.testdelivery_single),
]
