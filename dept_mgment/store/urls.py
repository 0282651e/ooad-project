from django.conf.urls import url
from django.conf.urls import include
from .views import show_bill_form

urlpatterns = [
    url(r'^$',show_bill_form, name='bill_form'),
]
