
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Customer_Service


# @receiver(post_save, sender=Customer_Service)
# def save_service_stock_from_custumer_service(sender, instance: Customer_Service, created, **kwargs):
#     if created:
#         print("kkkkk")
#         # print(kwargs.signal)
#         # stocklist = request.data["stock_list"]
#         # for service in servicelist:
#         #     CustomerService_Service.objects.create(
#         #         service_id=service, customer_service_id=id)

#         # for stock in stocklist:
#         #     CustomerService_Stock.objects.create(
#         #         stock_id=stock, customer_service_id=id)