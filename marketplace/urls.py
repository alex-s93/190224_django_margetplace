from django.urls import path, include

from rest_framework.routers import DefaultRouter

from marketplace.views.category_views import CategoryViewSet
from marketplace.views.product_views import (
    ProductListCreateView,
    ProductRetrieveUpdateDeleteGenericView,
)

router = DefaultRouter()
router.register('categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>', ProductRetrieveUpdateDeleteGenericView.as_view()),
]
