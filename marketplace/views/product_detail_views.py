from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)

from marketplace.models import ProductDetail
from marketplace.serializers.product_detail_serializer import (
    ProductDetailCreateUpdateSerializer,
    ProductDetailInfoSerializer
)


class ProductDetailListCreateView(ListCreateAPIView):
    queryset = ProductDetail.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductDetailCreateUpdateSerializer
        else:
            return ProductDetailInfoSerializer


class ProductDetailRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    __model = ProductDetail

    def get_object(self):
        return get_object_or_404(self.__model, pk=self.kwargs['pk'])

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return ProductDetailCreateUpdateSerializer
        else:
            return ProductDetailInfoSerializer

