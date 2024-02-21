from rest_framework import serializers
from .models import Invoice, InvoiceDetails


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = '__all__'
        extra_kwargs = {
            'price': {'required': False}
        }