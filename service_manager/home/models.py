from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    admin_representative = models.ForeignKey(
        "home.User", on_delete=models.CASCADE, related_name='companies_represented')
    email = models.EmailField(max_length=100)
    logo_url = models.URLField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    email = models.EmailField(max_length=100)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='users')

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Stock(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    expiration_date = models.DateTimeField()


class Customer_Service(models.Model):
    created_at = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class CustomerService_Service(models.Model):
    customer_service = models.ForeignKey(
        Customer_Service, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Stock_Service(models.Model):
    customer_service = models.ForeignKey(
        Customer_Service, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
