from rest_framework import serializers
from rest_framework.response import Response
from .models import (
    Client,
    Company,
    Service,
    Stock,
    Customer_Service,
    CustomerService_Service,
    CustomerService_Stock,
)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'




class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class CustomerServiceSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField(read_only=True)
    client_id =  serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source="client",
    )

    class Meta:
        model = Customer_Service
        fields = '__all__'

    def get_client(self, instance):
        serializer = ClientSerializer(instance.client)
        return serializer.data


class CustomerServiceServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService_Service
        fields = '__all__'


class StockServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerService_Stock
        fields = '__all__'
