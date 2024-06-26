from rest_framework.generics import ListCreateAPIView

from marketplace.models import Order
from marketplace.serializers.order_serializers import OrderSerializer


class OrderLisCreateView(ListCreateAPIView):

    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
