from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeView.as_view()),
    path('user/', views.UserView.as_view()),
    path('', views.index),
]
