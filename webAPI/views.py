from django.shortcuts import render
# import models
from .models import Employee, User
# import serializers
from .serializer import EmployeeSerializers, UserSerializers
# imports for list APIs
from rest_framework import generics
# import for filtering APIs
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# import for pagination
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class EmployeeView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('emp_id', 'firstname')
    search_fields = ('emp_id', 'firstname')


# class UserViewPagination(LimitOffsetPagination):
#     default_limit = 5
#     max_limit = 3


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('user_id', 'firstname')
    search_fields = ('user_id', 'firstname')
    # pagination_class = UserViewPagination


def index(request):
    return render(request, 'index.html')


