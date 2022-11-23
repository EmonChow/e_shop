from django.db.models import F, Sum
from rest_framework import serializers

from ..models import Customer, Vendor, Product, Purchase, Sales


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:

        model = Purchase
        fields = ['quantity', 'date', 'product', 'total_price', 'vendor_id']


class ProductSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class SalesSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Sales
        fields = ['quantity', 'date', 'product_id', 'total_price', 'customer_id']
