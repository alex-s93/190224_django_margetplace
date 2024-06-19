from rest_framework.viewsets import ModelViewSet
from marketplace.serializers.category_serializer import CategorySerializer
from marketplace.models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
