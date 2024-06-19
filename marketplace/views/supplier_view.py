from rest_framework.viewsets import ModelViewSet

from marketplace.serializers.supplier_serializer import SupplierSerializer
from marketplace.models import Supplier

class SupplierModelViewSet(ModelViewSet):

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
