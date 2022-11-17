from django.urls import path
from django.views.generic import TemplateView
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('customer-list', views.customer_list),
    path('customer/<int:id>', views.customer_details),
    path('vendor-list', views.vendor_list),
    path('vendor/<int:id>', views.vendor_details),
    path('product-list', views.product_list),
    path('product/<int:id>', views.product_view),
    path('purchase-list', views.purchase_list),
    path('purchase/<int:id>', views.purchase_view),
    path('sales-list', views.sales_list),
    path('sales/<int:id>', views.sales_view),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
