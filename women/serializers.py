import io

from rest_framework import serializers, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Women, Category


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
