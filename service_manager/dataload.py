# Carregamento de dados - script populando o banco de dados

import os
import django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_manager_api.settings")  # Substitua 'seu_projeto.settings' pelas configurações do seu projeto
django.setup()

from home.models import Client, Company, User, Service, Stock, Customer_Service, CustomerService_Service, CustomerService_Stock
from datetime import datetime

def load_data():
    clientes = ["Patricia","Amanda","José","Giovanna","Mariane","Juliana","Igor","Paulo"]
    empresas = ["Mecanico","Salão de beleza","PetShop","Dentista"]
    mecanico_servicos = ["troca de oleo","pintura","troca de correia","troca de pneu"]
    salao_servicos = ["corte","pintura","alisamento","escova"]
    petshop_servicos = ["banho","tosa","diaria","adestramento"]
    dentista_servicos = ["restauração","limpeza","clareamento","canal"]
    mecanico_estoque = ["Oleo","Pneu","Retrovisor","Capacete"]
    salao_estoque = ["Tinta","Shampoo","Fixador","Touca"]
    petshop_estoque = ["Brinquedo","Ração","Tapete higiênico","gravata"]
    dentista_estoque = ["Escova","Pasta de dente","Fio dental","Escova eletrica"]

    for cliente in clientes:
        cliente = Client(name=cliente, email=cliente+'@gmail.com', phone_number='123456789', cpf='12345678901')
        cliente.save()
    for empresa in empresas:
        company = Company(name=empresa, logo_url='https://example.com/logo1.png')
        company.save()

    # Criando instâncias de User
    user = User(name='Erika gerente1', is_admin=True, email='erika1@gmail.com', company_id=1)
    user.save()
    user = User(name='Erika gerente2', is_admin=True, email='erika2@gmail.com', company_id=2)
    user.save()
    user = User(name='Erika gerente3', is_admin=True, email='erika3@gmail.com', company_id=3)
    user.save()
    user = User(name='Erika gerente4', is_admin=True, email='erika4@gmail.com', company_id=4)
    user.save()

    
    for servico in mecanico_servicos:
        service1 = Service(title=servico, description='uma descrição sobre o serviço de '+servico, company_id=1, value=10)
        service1.save()

    
    for servico in salao_servicos:
        service1 = Service(title=servico, description='uma descrição sobre o serviço de '+servico, company_id=2,value=10)
        service1.save()

    
    for servico in petshop_servicos:
        service1 = Service(title=servico, description='uma descrição sobre o serviço de '+servico, company_id=3,value=10)
        service1.save()
    
    
    for servico in dentista_servicos:
        service1 = Service(title=servico, description='uma descrição sobre o serviço de '+servico, company_id=4,value=10)
        service1.save()

    for estoque in mecanico_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item '+estoque, expiration_date=timezone.now() , company_id=1, value=15)
        stock1.save()

    for estoque in salao_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item '+estoque, expiration_date=timezone.now() , company_id=2, value=15)
        stock1.save()
    
    for estoque in petshop_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item '+estoque, expiration_date=timezone.now() , company_id=3, value=15)
        stock1.save()
    
    for estoque in dentista_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item '+estoque, expiration_date=timezone.now() , company_id=4, value=15)
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



    CustomerService_Service.objects.create(customer_service=customer_service1, service_id=1)
    CustomerService_Service.objects.create(customer_service=customer_service1, service_id=2)
    CustomerService_Service.objects.create(customer_service=customer_service1, service_id=3)

    CustomerService_Stock.objects.create(customer_service=customer_service1, stock_id=1)
    CustomerService_Stock.objects.create(customer_service=customer_service1, stock_id=2)
    CustomerService_Stock.objects.create(customer_service=customer_service1, stock_id=2)

if __name__ == "__main__":
    load_data()
