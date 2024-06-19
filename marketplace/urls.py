from django.urls import path, include

from rest_framework.routers import DefaultRouter

from marketplace.views.category_views import CategoryViewSet
from marketplace.views.product_views import (
    ProductListCreateView,
    ProductRetrieveUpdateDeleteGenericView,
)
from marketplace.views.supplier_view import SupplierModelViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('supplier', SupplierModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>', ProductRetrieveUpdateDeleteGenericView.as_view()),
]
