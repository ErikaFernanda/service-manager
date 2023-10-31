from rest_framework import serializers
from rest_framework.response import Response
from .models import (
    Client,
    Company,
    User,
    Service,
    Stock,
    Customer_Service,
    CustomerService_Service,
    Stock_Service,
)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
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
    client = serializers.SerializerMethodField()

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
        model = Stock_Service
        fields = '__all__'