from django.contrib import admin
from .models import Client, Company, User, Service, Stock, Customer_Service, CustomerService_Service, CustomerService_Stock

admin.site.register(Client)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Service)
admin.site.register(Stock)
admin.site.register(Customer_Service)
admin.site.register(CustomerService_Service)
admin.site.register(CustomerService_Stock)