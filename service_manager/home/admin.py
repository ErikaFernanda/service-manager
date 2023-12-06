from django.contrib import admin
from .models import Client, Company, Service, Stock, Customer_Service, CustomerService_Service, CustomerService_Stock, Customer_Service_Note

admin.site.register(Client)
admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Stock)
admin.site.register(Customer_Service)
admin.site.register(CustomerService_Service)
admin.site.register(CustomerService_Stock)
admin.site.register(Customer_Service_Note)