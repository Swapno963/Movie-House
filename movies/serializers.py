from rest_framework import serializers
from . import models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MoviesModel
        fields = '__all__'
