import os
import django
from django.utils import timezone
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service_manager_api.settings")
django.setup()
from django.db import connection
from datetime import datetime
from home.models import Client, Company, Service, Stock, Customer_Service, CustomerService_Service, CustomerService_Stock
from login.models import User, CustomUserManager
from django.contrib.auth import get_user_model


def load_data():
    clientes_c1 = ["Evelyn Sara Silva", "Amanda dos Santos Bernando"]
    clientes_c2 = ["José da Silva",
                   "Giovanna Karla Oliveira", "Paulo Santos Sousa"]
    clientes_c3 = ["Mariane Felix Santos",
                   "Juliana Beatriz Sales", "Igor Carvalho Lopes"]
    clientes_c4 = ["Eduardo Campos Neto", "Larissa Lima Gomes"]

    empresas = ["PetShop e Veterinário", "Gira Mundo Moto Peças - Mecânico",
                "Bella Dona - Salão de beleza", "DuPallets - Móveis e Criações Sustentáveis",]
    empresas_logo = ["https://img.freepik.com/vetores-premium/design-de-logotipo-de-cachorrinho-fofo-de-pet-shop_680355-30.jpg",
                     "https://seocity.com.br/wp-content/uploads/2019/08/logo-giramundo.jpg",
                     "https://www.disksc.com.br/files/08_04_2016_14_34_55_5ae56546d9e57bb4d0be8a6b5436f52c.jpg",
                     "https://dupallets.com.br/wp-content/uploads/2021/04/logo-ok-300x133.png"]

    mecanico_servicos = ["Troca de óleo", "Pintura",
                         "Troca de correia", "Troca de pneu"]
    salao_servicos = ["Corte", "Pintura", "Progressiva", "Escova"]
    petshop_servicos = ["Banho", "Tosa", "Diária", "Adestramento"]
    movelaria_servicos = [
        "Conserto", "Produção de Praleleira 2x2", "Produção de Mesa 3x3", "Envernizar"]

    mecanico_estoque = ["Oleo", "Pneu", "Água destilada", "Capacete"]
    salao_estoque = ["Tinta", "Shampoo", "Fixador", "Touca"]
    movelaria_estoque = ["Tinta", "Verniz", "Prateleira 1x1", "Decoração"]
    petshop_estoque = ["Brinquedo", "Ração", "Tapete higiênico", "gravata"]

    Client.objects.all().delete()
    Company.objects.all().delete()
    User.objects.all().delete()
    Service.objects.all().delete()
    Customer_Service.objects.all().delete()
    CustomerService_Service.objects.all().delete()
    CustomerService_Stock.objects.all().delete()

    with connection.cursor() as cursor:
        cursor.execute("TRUNCATE TABLE home_client RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE home_company RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE login_user RESTART IDENTITY CASCADE;")
        cursor.execute("TRUNCATE TABLE home_service RESTART IDENTITY CASCADE;")
        cursor.execute(
            "TRUNCATE TABLE home_customer_service RESTART IDENTITY CASCADE;")
        cursor.execute(
            "TRUNCATE TABLE home_customerservice_service RESTART IDENTITY CASCADE;")
        cursor.execute(
            "TRUNCATE TABLE home_customerservice_stock RESTART IDENTITY CASCADE;")

    count = 0
    for empresa in empresas:
        company = Company(
            name=empresa, logo_url=empresas_logo[count], cnpj="00.360.305/0001-04")
        company.save()
        count += 1

    for cliente in clientes_c1:
        cliente = Client(name=cliente, email=f'{cliente.split()[0]}@gmail.com',
                         phone_number=f'(84) 99{count+10}-45{count+1}8', cpf='123.456.789-01', company_id=1)
        cliente.save()
    for cliente in clientes_c2:
        cliente = Client(name=cliente, email=f'{cliente.split()[0]}@gmail.com',
                         phone_number=f'(84) 99{count+10}-45{count+1}8', cpf='123.456.789-01', company_id=2)
        cliente.save()
    for cliente in clientes_c3:
        cliente = Client(name=cliente, email=f'{cliente.split()[0]}@gmail.com',
                         phone_number=f'(84) 99{count+10}-45{count+1}8', cpf='123.456.789-01', company_id=3)
        cliente.save()
    for cliente in clientes_c4:
        cliente = Client(name=cliente, email=f'{cliente.split()[0]}@gmail.com',
                         phone_number=f'(84) 99{count+10}-45{count+1}8', cpf='123.456.789-01', company_id=4)
        cliente.save()

    
    UserManager = get_user_model()


    user = UserManager(name='Erika gerente1', username="admin1", is_admin=True,
                email='erika1@gmail.com', company_id=1)
    user.set_password("admin")
    user.save()
    user = UserManager(name='Erika gerente2', username="admin2", is_admin=True,
                email='erika2@gmail.com', company_id=2)
    user.set_password("admin")
    user.save()
    user = UserManager(name='Erika gerente3', username="admin3",  is_admin=True,
                email='erika3@gmail.com', company_id=3)
    user.set_password("admin")
    user.save()
    user = UserManager(name='Erika gerente4', username="admin4",  is_admin=True,
                email='erika4@gmail.com', company_id=4)
    user.set_password("admin")
    user.save()
    count=1
    for servico in petshop_servicos:
        service1 = Service(
            title=servico, description='Uma descrição sobre o serviço de '+servico, company_id=1, value=count*25.75)
        service1.save()
        count+=1

    for servico in mecanico_servicos:
        service1 = Service(
            title=servico, description='Uma descrição sobre o serviço de '+servico, company_id=2, value=count*25.75)
        service1.save()
        count+=1

    for servico in salao_servicos:
        service1 = Service(
            title=servico, description='Uma descrição sobre o serviço de '+servico, company_id=3, value=count*25.75)
        service1.save()
        count+=1

    for servico in movelaria_servicos:
        service1 = Service(
            title=servico, description='Uma descrição sobre o serviço de '+servico, company_id=4, value=count*25.75)
        service1.save()
        count+=1

    for estoque in petshop_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item ' +
                       estoque, expiration_date=timezone.now(), company_id=1, value=15)
        stock1.save()
        count+=1

    for estoque in mecanico_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item ' +
                       estoque, expiration_date=timezone.now(), company_id=2, value=15)
        stock1.save()
        count+=1

    for estoque in salao_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item ' +
                       estoque, expiration_date=timezone.now(), company_id=3, value=15)
        stock1.save()
        count+=1

    for estoque in movelaria_estoque:
        stock1 = Stock(title=estoque, description='Descrição do item ' +
                       estoque, expiration_date=timezone.now(), company_id=4, value=15)
        stock1.save()
        count+=1

    # customer_service1 = Customer_Service(client_id=1, company_id=1)
    # customer_service1.save()
    # customer_service2 = Customer_Service(client_id=2, company_id=1)
    # customer_service2.save()
    # customer_service3 = Customer_Service(client_id=3, company_id=1)
    # customer_service3.save()
    # customer_service4 = Customer_Service(client_id=4, company_id=1)
    # customer_service4.save()
    # customer_service5 = Customer_Service(client_id=5, company_id=1)
    # customer_service5.save()
    # customer_service6 = Customer_Service(client_id=6, company_id=1)
    # customer_service6.save()
    # customer_service7 = Customer_Service(client_id=7, company_id=1)
    # customer_service7.save()
    # customer_service8 = Customer_Service(client_id=8, company_id=1)
    # customer_service8.save()

    # CustomerService_Service.objects.create(
    #     customer_service=customer_service1, service_id=1)
    # CustomerService_Service.objects.create(
    #     customer_service=customer_service1, service_id=2)
    # CustomerService_Service.objects.create(
    #     customer_service=customer_service1, service_id=3)

    # CustomerService_Stock.objects.create(
    #     customer_service=customer_service1, stock_id=1, quatity=3)
    # CustomerService_Stock.objects.create(
    #     customer_service=customer_service1, stock_id=2, quatity=2)
    # CustomerService_Stock.objects.create(
    #     customer_service=customer_service1, stock_id=2, quatity=5)


if __name__ == "__main__":
    load_data()
