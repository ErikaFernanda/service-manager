from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from django.urls import include, path

router = DefaultRouter()
router.register('company', views.CompanyListView)
router.register('customer_service', views.CustomerServiceListView)
router.register('service', views.ServiceListView)
router.register('client', views.ClientListView)
router.register('stock', views.StockListView)






urlpatterns = [
    path('', include(router.urls)),
    path('home', views.home, name='home'),
    path('generate_pdf', views.generate_pdf, name='generate_pdf'),
    # path('customer_service', views.CustomerServiceListView.as_view(),
    #      name='customer service'),
    path('customer_service_service', views.CustomerServiceServiceListView.as_view(
    ), name='customer service service'),
    path('customer_service_stock', views.CustomerServiceStockListView.as_view(
    ), name='customer service stock'),
    # path('service', views.ServiceListView.as_view(), name='service'),
    # path('company', views.CompanyListView.as_view(),name= 'company'),
    # path('client', views.ClientListView.as_view(), name='client'),
    # path('stock', views.StockListView.as_view(), name='stock'),

]
