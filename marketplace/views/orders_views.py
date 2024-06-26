from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from marketplace.models import Order
from marketplace.serializers.order_serializers import OrderSerializer
from marketplace.permissions.customer_permission import IsCustomerOrReadOnly


class OrderLisCreateView(ListCreateAPIView):
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)


class OrderRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsCustomerOrReadOnly]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user)
