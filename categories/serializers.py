from rest_framework import serializers
from . import models

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryModel
        fields = '__all__'