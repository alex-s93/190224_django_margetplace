from rest_framework import serializers

from marketplace.models import OrderItem
from marketplace.serializers.product_serializer import ProductDetailSerializer
from marketplace.serializers.order_serializers import OrderSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()
    order = OrderSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderItemCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

    def validate_quantity(self, value):
        if value > 1000:
            return serializers.ValidationError(
                "Quantity must be less or equal than 1000"
            )

        return value
