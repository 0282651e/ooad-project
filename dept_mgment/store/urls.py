from django.conf.urls import include, url

from .views import BillView, HomeView, OrderView, SupplierView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='store_home'),
    url(r'^bill/$', BillView.as_view(), name='store_bill'),
    url(r'^order/$',OrderView.as_view(),name='store_order'),
    url(r'^supplier/$',SupplierView.as_view(),name='store_supplier')
]
