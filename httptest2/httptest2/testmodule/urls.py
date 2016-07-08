from django.conf.urls import url
from httptest2.testmodule import views

urlpatterns = [
    url(r'^index', views.display_all),
    url(r'^inserttestmodel', views.insert_all),
]
