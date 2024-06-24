from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    get_object_or_404,
)


from marketplace.models import Product
from marketplace.serializers.product_serializer import (
    ProductDetailSerializer,
    ProductCreateSerializer
)


class ProductRetrieveUpdateDeleteGenericView(RetrieveUpdateDestroyAPIView):
    __model = Product

    def get_object(self):
        return get_object_or_404(self.__model, pk=self.kwargs['pk'])

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductDetailSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ProductCreateSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        else:
            return ProductDetailSerializer
