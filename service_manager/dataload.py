# Carregamento de dados - script populando o banco de dados

import os
import django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_manager_api.settings")  # Substitua 'seu_projeto.settings' pelas configurações do seu projeto
django.setup()

from home.models import Client, Company, User, Service, Stock, Customer_Service, CustomerService_Service, Stock_Service
from datetime import datetime

def load_data():
    # Criando instâncias de Client
    client1 = Client(name='Cliente 1', email='cliente1@example.com', phone_number='123456789', cpf='12345678901')
    client1.save()

    # Criando instâncias de Company
    company1 = Company(name='Empresa 1', logo_url='https://example.com/logo1.png')
    company1.save()

    # Criando instâncias de User
    user1 = User(name='Usuário 1', is_admin=True, email='user1@example.com', company=company1)
    user1.save()

    # Criando instâncias de Service
    service1 = Service(title='Serviço 1', description='Descrição do Serviço 1', company=company1)
    service1.save()

    # Criando instâncias de Stock
    stock1 = Stock(title='Estoque 1', description='Descrição do Estoque 1', expiration_date=timezone.now() , company=company1)
    stock1.save()

    # Criando instâncias de Customer_Service
    customer_service1 = Customer_Service(client=client1, company=company1)
    customer_service1.save()

    # Relacionando Customer_Service com Service
    CustomerService_Service.objects.create(customer_service=customer_service1, service=service1)

    # Relacionando Customer_Service com Stock
    Stock_Service.objects.create(customer_service=customer_service1, stock=stock1)

if __name__ == "__main__":
    load_data()
