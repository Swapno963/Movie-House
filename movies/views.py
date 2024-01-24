from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

class MovieViewset(viewsets.ModelViewSet):
    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer


