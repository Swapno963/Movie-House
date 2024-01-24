from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from . import models
from . import serializers

# Create your views here.
class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer