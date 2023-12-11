
from django.shortcuts import render
from rest_framework import generics
from .models import (
    Client,
    Company,
    Service,
    Stock,
    Customer_Service,
    CustomerService_Service,
    CustomerService_Stock,
    Customer_Service_Note
)
from .serializers import (
    ClientSerializer,
    CompanySerializer,
    ServiceSerializer,
    StockSerializer,
    CustomerServiceSerializer,
    CustomerServiceServiceSerializer,
    CustomerServiceStockSerializer

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
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from django.http import QueryDict
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

@csrf_exempt
def generate_pdf(request):
    

    if request.method == 'POST':

        line = 700
        column = 50
          
        body_content = request.body.decode('utf-8')
        chave_json = json.loads(body_content)
        id_atendimento = chave_json.get('customer_service_id', '')
        cs =Customer_Service.objects.get(id=id_atendimento)
        data_hora_formatada = timezone.localtime(cs.created_at).strftime('%d/%m/%Y - %H:%M:%S')
        data_emissao = data_hora_formatada
        detalhes_produtos = CustomerService_Stock.objects.filter(customer_service=id_atendimento)
        detalhes_servicos = CustomerService_Service.objects.filter(customer_service=id_atendimento)
        numero_nota = f'1923{cs.id}'

        total_nota = sum(item.quantity * item.stock.value
                         for item in detalhes_produtos)+sum(item.service.value
                                                            for item in detalhes_servicos)

        # Criar um buffer para o PDF
        buffer = BytesIO()

        # Criar o PDF no buffer
        pdf_canvas = canvas.Canvas(buffer, pagesize=(600, 800))
        pdf_canvas.setFont("Helvetica-Bold", 14)
        pdf_canvas.drawString(column, line, f'{cs.company.name.upper()} - CNPJ {cs.company.cnpj}')
        pdf_canvas.setFont("Helvetica-Bold", 14)
        line=line-25     
        pdf_canvas.drawString(column, line, f'Nota Fiscal #{numero_nota}')
        line=line-20 
        pdf_canvas.drawString(column, line, f'Data de Emissão: {data_emissao}')
        line=line-20
        pdf_canvas.drawString(column, line, f'Cliente: {cs.client.name} - CPF {cs.client.cpf}')

        line=line-40
        pdf_canvas.setFont("Helvetica", 12)

        pdf_canvas.drawString(column, line, 'Detalhes de serviços:')
        for item in detalhes_servicos:
            line -= 20
            pdf_canvas.drawString(
                column+20, line, f'{item.service.title}: R${item.service.value:.2f}')
        

        line=line-40 
        pdf_canvas.drawString(column, line, 'Detalhes do Produto:')
        for item in detalhes_produtos:
            total_item = item.quantity * item.stock.value
            line -= 20
            pdf_canvas.drawString(
                column+20, line, f'{item.stock.title}: {item.quantity} x R${item.stock.value:.2f} = R${total_item:.2f}')

        line=line-40 
        # Total da nota fiscal
        pdf_canvas.drawString(column, line,
                              f'Total da Nota Fiscal: R${total_nota:.2f}')

        pdf_canvas.save()

        # Resetar o buffer para o início
        buffer.seek(0)

        # Criar uma resposta HTTP com o PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="nota_fiscal_{numero_nota}.pdf"'
        response.write(buffer.read())
        # buffer.seek(0)
        # pdf_temp = ContentFile(buffer.read())
        # pdf_temp.name = 'arquivo_temp.pdf'
        # Customer_Service_Note.objects.create(name="um nome2", file=pdf_temp)
        return response
    else:
        return HttpResponse("Método não permitido.", status=405)


@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')


class ClientListView(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.serializer_class.Meta.model.objects.filter(
            company_id=user.company_id)
        return queryset

    def create(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        request.data["company"] = company_id
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        request.data["company"] = company_id
        return super().update(request, *args, **kwargs)

# class CompanyListView(generics.ListCreateAPIView):


class CompanyListView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ServiceListView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.serializer_class.Meta.model.objects.filter(
            company_id=user.company_id)
        return queryset

    def create(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        request.data["company"] = company_id
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        request.data["company"] = company_id
        return super().update(request, *args, **kwargs)


class StockListView(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.serializer_class.Meta.model.objects.filter(
            company_id=user.company_id)
        return queryset

    def create(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        request.data["company"] = company_id
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        request.data["company"] = company_id
        return super().update(request, *args, **kwargs)


class CustomerServiceListView(ModelViewSet):
    queryset = Customer_Service.objects.all()
    serializer_class = CustomerServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Customer_Service.objects.filter(company_id=user.company_id)
        return queryset

    def create(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        request.data["company"] = company_id

        response = super().create(request, *args, **kwargs)
        id = response.data.get('id', None)

        servicelist = request.data["service_list"]
        stocklist = request.data["stock_list"]
        for service in servicelist:
            CustomerService_Service.objects.create(
                service_id=service, customer_service_id=id)

        for stock in stocklist:

            CustomerService_Stock.objects.create(
                stock_id=stock["id"], quantity=stock["quantity"], customer_service_id=id)
        service_list = CustomerService_Service.objects.filter(
            customer_service_id=id)
        stock_list = CustomerService_Stock.objects.filter(
            customer_service_id=id)
        response.data['service_list'] = CustomerServiceServiceSerializer(
            service_list, many=True).data
        response.data['stock_list'] = CustomerServiceStockSerializer(
            stock_list, many=True).data
        return response

    def update(self, request, *args, **kwargs):
        company_id = self.request.user.company_id
        request.data["company"] = company_id
        return super().update(request, *args, **kwargs)


class CustomerServiceServiceListView(generics.ListCreateAPIView):
    queryset = CustomerService_Service.objects.all()
    serializer_class = CustomerServiceServiceSerializer


class CustomerServiceStockListView(generics.ListCreateAPIView):
    queryset = CustomerService_Stock.objects.all()
    serializer_class = CustomerServiceStockSerializer
