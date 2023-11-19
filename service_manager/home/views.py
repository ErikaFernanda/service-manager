
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
    CustomerService_Stock,
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
from datetime import datetime
import json

def generate_pdf(request):
    numero_nota = '0000001'

    if request.method == 'POST':
        data_hora_formatada = datetime.now().strftime('%d/%m/%Y - %H:%M:%S')
        data_emissao = data_hora_formatada
        chave = list(request.POST.keys())[0]

        # Analise a chave como JSON
        chave_json = json.loads(chave)
        nome_cliente = chave_json.get('cliente', '')
        servicos_ids = chave_json.get('servicos', '')
        produtos_ids = chave_json.get('produtos', '')
        detalhes_servicos=Service.objects.filter(id__in=servicos_ids)
        detalhes_produtos = Stock.objects.filter(id__in=produtos_ids)
        

        # Total da nota fiscal
        total_nota = sum(2* item.value
                         for item in detalhes_produtos)+sum(item.value
                         for item in detalhes_servicos)

        # Criar um buffer para o PDF
        buffer = BytesIO()

        # Criar o PDF no buffer
        pdf_canvas = canvas.Canvas(buffer, pagesize=(600, 800))

        pdf_canvas.setFont("Helvetica-Bold", 14)
        pdf_canvas.drawString(200, 750, f'Nota Fiscal #{numero_nota}')
        pdf_canvas.drawString(200, 730, f'Data de Emissão: {data_emissao}')
        pdf_canvas.drawString(200, 710, f'Cliente: {nome_cliente}')

        y_position = 670
        pdf_canvas.setFont("Helvetica", 12)

        pdf_canvas.drawString(50, y_position, 'Detalhes de serviços:')
        for item in detalhes_servicos:
            y_position -= 20
            pdf_canvas.drawString(
                70, y_position, f'{item.title}: R${item.value:.2f}')
        y_position = 570



        pdf_canvas.drawString(50, y_position, 'Detalhes do Produto:')
        for item in detalhes_produtos:
            total_item = 2* item.value
            y_position -= 20
            pdf_canvas.drawString(
                70, y_position, f'{item.title}: 2 x R${item.value:.2f} = R${total_item:.2f}')

        # Total da nota fiscal
        pdf_canvas.drawString(50, y_position - 30,
                              f'Total da Nota Fiscal: R${total_nota:.2f}')

        # Salvar o PDF
        pdf_canvas.save()

        # Resetar o buffer para o início
        buffer.seek(0)

        # Criar uma resposta HTTP com o PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="nota_fiscal_{numero_nota}.pdf"'
        response.write(buffer.read())

        return response
    else:
        return HttpResponse("Método não permitido.", status=405)


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


class CustomerServiceStockListView(generics.ListCreateAPIView):
    queryset = CustomerService_Stock.objects.all()
    serializer_class = StockServiceSerializer
