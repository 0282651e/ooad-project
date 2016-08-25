from django.conf.urls import include, url

from .views import BillView, HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='store_home'),
    url(r'^bill/$', BillView.as_view(), name='store_bill')
]
