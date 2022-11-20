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

    class Meta:
        model = Purchase
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    purchase = PurchaseSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"
