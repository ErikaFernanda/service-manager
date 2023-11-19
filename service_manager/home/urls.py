from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('generate_pdf', views.generate_pdf, name='generate_pdf'),
    path('customer_service', views.CustomerServiceListView.as_view(),name= 'customer service'),
    path('customer_service_service',views.CustomerServiceServiceListView.as_view(),name='customer service service'),
    path('customer_service_stock',views.CustomerServiceStockListView.as_view(),name='customer service stock'),
    path('service', views.ServiceListView.as_view(),name= 'service'),
    path('client', views.ClientListView.as_view(),name= 'client'),
    path('stock', views.StockListView.as_view(),name= 'stock'),
    
]
