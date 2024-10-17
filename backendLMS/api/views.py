from django.shortcuts import render
from rest_framework import viewsets
from api.models import Books
from api.serializers import BooksSerializers
# Create your views here.


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers