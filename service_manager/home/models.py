from typing import Iterable, Optional
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    admin_representative = models.ForeignKey(
        "login.User", on_delete=models.CASCADE, related_name='companies_represented', blank=True, null=True)
    logo_url = models.URLField(max_length=200)
    cnpj =  models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class CompanyUser(models.Model):
    user = models.ForeignKey(
        "login.User", on_delete=models.CASCADE, related_name='companies_users', blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name+" "+self.company.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    created_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Stock(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    expiration_date = models.DateTimeField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Customer_Service(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client} - {self.company}"

class CustomerService_Service(models.Model):
    customer_service = models.ForeignKey(
        Customer_Service, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.service.title} - {self.service.company.name}"


class CustomerService_Stock(models.Model):
    customer_service = models.ForeignKey(
        Customer_Service, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.stock.title} - {self.service.company.name}"

class Customer_Service_Note(models.Model):
    name = models.CharField(max_length=255)
    # file = models.BinaryField()
    file=models.FileField(upload_to='pdfs/')

