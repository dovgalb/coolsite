import io

from rest_framework import serializers, generics
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = '__all__'

