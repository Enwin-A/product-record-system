from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'colour', 'part_number', 
                 'size_mm', 'description', 'image_url',
                 'created_at', 'updated_at']
        extra_kwargs = {
            'part_number': {'validators': [
                UniqueValidator(queryset=Product.objects.all())
            ]}
        }
