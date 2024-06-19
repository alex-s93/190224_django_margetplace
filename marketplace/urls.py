from django.urls import path

from marketplace.views.product_views import (
    ProductListCreateView,
    ProductRetrieveUpdateDeleteGenericView,
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view()),
    path('products/<int:pk>', ProductRetrieveUpdateDeleteGenericView.as_view()),
]
