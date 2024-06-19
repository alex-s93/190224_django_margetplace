from rest_framework.generics import RetrieveUpdateDestroyAPIView, get_object_or_404

from marketplace.models import Product
from marketplace.serializers.product_serializer import ProductDetailSerializer, ProductCreateSerializer


class RetrieveUpdateDeleteGenericView(RetrieveUpdateDestroyAPIView):
    __model = Product

    def get_object(self):
        return get_object_or_404(self.__model, pk=self.kwargs['pk'])

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProductDetailSerializer
        elif self.request.method in ['PUT', 'PATCH']:
            return ProductCreateSerializer
