
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
from django_filters.rest_framework import DjangoFilterBackend

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse

def generate_pdf(request):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)

    pdf.drawString(100, 750, "Hello, this is a PDF with ReportLab!")
    pdf.drawString(100, 730, "You can add text, shapes, images, etc.")

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="output.pdf"'
    return response




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
    filter_backends = [DjangoFilterBackend]  
    filterset_fields = ['company']

class CustomerServiceServiceListView(generics.ListCreateAPIView):
    queryset = CustomerService_Service.objects.all()
    serializer_class = CustomerServiceServiceSerializer
    



class StockServiceListView(generics.ListCreateAPIView):
    queryset = Stock_Service.objects.all()
    serializer_class = StockServiceSerializer
