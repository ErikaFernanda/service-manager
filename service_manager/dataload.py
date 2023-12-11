import django
from django.utils import timezone
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_manager_api.settings")
django.setup()

from django.db import connection
from datetime import datetime
from home.models import Client, Company, Service, Stock, Customer_Service, CustomerService_Service, CustomerService_Stock
from login.models import User





def load_data():
    clientes = ["Patricia", "Amanda", "José", "Giovanna",
                "Mariane", "Juliana", "Igor", "Paulo"]
    
    empresas = ["Mecanico", "Salão de beleza", "PetShop", "Dentista",
                "Mecanico1", "Salão de beleza1", "PetShop1", "Dentista1", "Mecanico2", "Salão de beleza2", "PetShop2",
                "Dentista2", "Mecanico3", "Salão de beleza3", "PetShop3", "Dentista3", "Mecanico4", "Salão de beleza4", "PetShop4", "Dentista4", "Mecanico", "Salão de beleza", "PetShop", "Dentista",
                "Mecanico1", "Salão de beleza1", "PetShop1", "Dentista1", "Mecanico2", "Salão de beleza2", "PetShop2",
                "Dentista2", "Mecanico3", "Salão de beleza3", "PetShop3", "Dentista3", "Mecanico4", "Salão de beleza4", "PetShop4", "Dentista4"]
    mecanico_servicos = ["troca de oleo", "pintura",
                         "troca de correia", "troca de pneu"]
    salao_servicos = ["corte", "pintura", "alisamento", "escova"]
    petshop_servicos = ["banho", "tosa", "diaria", "adestramento"]
    dentista_servicos = ["restauração", "limpeza", "clareamento", "canal"]
    mecanico_estoque = ["Oleo", "Pneu", "Retrovisor", "Capacete"]
    salao_estoque = ["Tinta", "Shampoo", "Fixador", "Touca"]
    petshop_estoque = ["Brinquedo", "Ração", "Tapete higiênico", "gravata"]
    dentista_estoque = ["Escova", "Pasta de dente",
                        "Fio dental", "Escova eletrica"]

    Client.objects.all().delete()
    Company.objects.all().delete()
    User.objects.all().delete()
    Service.objects.all().delete()

    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE home_client RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE home_company RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE login_user RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE home_service RESTART IDENTITY CASCADE;")

    for empresa in empresas:
        company = Company(
            name=empresa, logo_url='https://img.freepik.com/vetores-premium/design-de-logotipo-de-cachorrinho-fofo-de-pet-shop_680355-30.jpg', cnpj="00.360.305/0001-04")
        company.save()

    for cliente in clientes:
        cliente = Client(name=cliente, email=cliente+'@gmail.com',
                         phone_number='123456789', cpf='12345678901', company_id=1)
        cliente.save()

    # Criando instâncias de User
    user = User(name='Erika gerente1', is_admin=True,
                email='erika1@gmail.com', company_id=1, username="erika1")
    user.save()
    user = User(name='Erika gerente2', is_admin=True,
                email='erika2@gmail.com', company_id=2, username="erika2")
    user.save()
    user = User(name='Erika gerente3', is_admin=True,
                email='erika3@gmail.com', company_id=3, username="erika3")
    user.save()
    user = User(name='Erika gerente4', is_admin=True,
                email='erika4@gmail.com', company_id=4, username="erika4")
    user.save()

    for servico in mecanico_servicos:
        service1 = Service(
            title=servico, description='uma descrição sobre o serviço de '+servico, company_id=1, value=10)
        service1.save()

    for servico in salao_servicos:
        service1 = Service(
            title=servico, description='uma descrição sobre o serviço de '+servico, company_id=2, value=10)
        service1.save()

    for servico in petshop_servicos:
        service1 = Service(
            title=servico, description='uma descrição sobre o serviço de '+servico, company_id=3, value=10)
        service1.save()

    for servico in dentista_servicos:
        service1 = Service(
            title=servico, description='uma descrição sobre o serviço de '+servico, company_id=4, value=10)
        service1.save()

    for estoque in mecanico_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item ' +
                       estoque, expiration_date=timezone.now(), company_id=1, value=15)
        stock1.save()

    for estoque in salao_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item ' +
                       estoque, expiration_date=timezone.now(), company_id=2, value=15)
        stock1.save()

    for estoque in petshop_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item ' +
                       estoque, expiration_date=timezone.now(), company_id=3, value=15)
        stock1.save()

    for estoque in dentista_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item ' +
                       estoque, expiration_date=timezone.now(), company_id=4, value=15)
        stock1.save()

    # Criando instâncias de Customer_Service
    customer_service1 = Customer_Service(client_id=1, company_id=1)
    customer_service1.save()
    customer_service2 = Customer_Service(client_id=2, company_id=1)
    customer_service2.save()
    customer_service3 = Customer_Service(client_id=3, company_id=1)
    customer_service3.save()
    customer_service4 = Customer_Service(client_id=4, company_id=1)
    customer_service4.save()
    customer_service5 = Customer_Service(client_id=5, company_id=1)
    customer_service5.save()
    customer_service6 = Customer_Service(client_id=6, company_id=1)
    customer_service6.save()
    customer_service7 = Customer_Service(client_id=7, company_id=1)
    customer_service7.save()
    customer_service8 = Customer_Service(client_id=8, company_id=1)
    customer_service8.save()

    CustomerService_Service.objects.create(
        customer_service=customer_service1, service_id=1)
    CustomerService_Service.objects.create(
        customer_service=customer_service1, service_id=2)
    CustomerService_Service.objects.create(
        customer_service=customer_service1, service_id=3)

    CustomerService_Stock.objects.create(
        customer_service=customer_service1, stock_id=1, quantity=3)
    CustomerService_Stock.objects.create(
        customer_service=customer_service1, stock_id=2, quantity=2)
    CustomerService_Stock.objects.create(
        customer_service=customer_service1, stock_id=2, quantity=5)


if __name__ == "__main__":
    load_data()
