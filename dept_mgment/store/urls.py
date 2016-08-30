from django.conf.urls import include, url

from .views import MakeBill, HomeView, OrderView, SupplierView, ViewBill

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='store_home'),
    url(r'^bill/$', MakeBill.as_view(), name='store_bill'),
    url(r'^order/$',OrderView.as_view(),name='store_order'),
    url(r'^supplier/$',SupplierView.as_view(),name='store_supplier'),
    url(r'^viewbill/$',ViewBill.as_view(),name='store_viewbill')
]
