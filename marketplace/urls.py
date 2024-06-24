from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from marketplace.views.category_views import CategoryViewSet
from marketplace.views.product_views import (
    ProductListCreateView,
    ProductRetrieveUpdateDeleteGenericView,
)
from marketplace.views.product_detail_views import (
    ProductDetailListCreateView,
    ProductDetailRetrieveUpdateDeleteView
)
from marketplace.views.supplier_view import SupplierModelViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('supplier', SupplierModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>/', ProductRetrieveUpdateDeleteGenericView.as_view()),
    path('product-details/', ProductDetailListCreateView.as_view()),
    path('product-details/<int:pk>/', ProductDetailRetrieveUpdateDeleteView.as_view()),
    path('login/', obtain_auth_token),
    path('get-token-now/', TokenObtainPairView.as_view()),
    path('get-token-now/refresh/', TokenRefreshView.as_view())
]
