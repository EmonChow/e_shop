from django.db.models import F
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer, VendorSerializer, ProductSerializer, PurchaseSerializer, SalesSerializer
from ..models import Customer, Vendor, Product, Purchase, Sales


class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerView(generics.RetrieveDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@api_view(['GET', 'POST'])
def vendor_list(request):
    if request.method == "GET":
        vendorlist = Vendor.objects.all()
        serializer = VendorSerializer(vendorlist, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def vendor_details(request, id):
    if request.method == "GET":
        try:
            vendorlist = Vendor.objects.get(pk=id)
        except Vendor.DoesNotExist:
            return Response({'error': "Vendor doesnt found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = VendorSerializer(vendorlist)
        return Response(serializer.data)
    if request.method == "PUT":
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        vendorlist = Vendor.objects.get(pk=id)
        vendorlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        productlist = Product.objects.all()
        serializer = ProductSerializer(productlist, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def product_view(request, id):
    if request.method == 'GET':
        try:
            productlist = Product.objects.get(pk=id)
        except Product.DoesNotExist:
            return Response({'error': "Product doesnt found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = ProductSerializer(productlist)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        productlist = Product.objects.get(pk=id)
        productlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def purchase_list(request):
    if request.method == 'GET':
        purchaselist = Purchase.objects.all()
        serializer = PurchaseSerializer(purchaselist, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def purchase_view(request, id):
    if request.method == 'GET':
        try:
            purchase = Purchase.objects.get(pk=id)
        except Purchase.DoesNotExist:
            return Response({'error': "Purchase doesnt found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = PurchaseSerializer(purchase)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        purchase = Purchase.objects.get(pk=id)
        purchase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def sales_list(request):
    if request.method == 'GET':
        sales = Sales.objects.all()
        serializer = SalesSerializer(sales, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def sales_view(request, id):
    if request.method == 'GET':
        try:
            sales = Sales.objects.get(pk=id)
        except Sales.DoesNotExist:
            return Response({'error': "Sales doesnt found"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = SalesSerializer(sales)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = SalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        sales = Sales.objects.get(pk=id)
        sales.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
