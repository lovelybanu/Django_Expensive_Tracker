from django.urls import path
from . import views

urlpatterns = [
    path('home', views.Home, name='home'),
    path('delete/<int:id>/', views.delete_transaction, name='delete_transaction'),
]