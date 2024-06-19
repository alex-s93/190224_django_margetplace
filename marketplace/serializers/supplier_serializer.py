import re

from rest_framework import serializers

from marketplace.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supplier
        fields = '__all__'


    def validate_name(self, value):

        if len(value) < 3:
            raise serializers.ValidationError('Name must be at least 3 characters')

        if not re.match(r'^[A-Za-z_]+$', value):
            raise serializers.ValidationError('Name must contain only alphabet')

        return value
