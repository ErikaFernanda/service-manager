
from django.shortcuts import render
from rest_framework import generics
from .models import (
    Client,
    Company,
    User,
    Service,
    Stock,
    Customer_Service,
    CustomerService_Service,
    Stock_Service,
)
from .serializers import (
    ClientSerializer,
    CompanySerializer,
    UserSerializer,
    ServiceSerializer,
    StockSerializer,
    CustomerServiceSerializer,
    CustomerServiceServiceSerializer,
    StockServiceSerializer,
)


def home(request):
    return render(request, 'home/home.html')


class ClientListView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CompanyListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ServiceListView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class StockListView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class CustomerServiceListView(generics.ListCreateAPIView):
    queryset = Customer_Service.objects.all()
    serializer_class = CustomerServiceSerializer


class CustomerServiceServiceListView(generics.ListCreateAPIView):
    queryset = CustomerService_Service.objects.all()
    serializer_class = CustomerServiceServiceSerializer


class StockServiceListView(generics.ListCreateAPIView):
    queryset = Stock_Service.objects.all()
    serializer_class = StockServiceSerializer
