from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import HeroSerializer
from .models import Heros


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Heros.objects.all().order_by('name')
    serializer_class = HeroSerializer
