from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_principal, name='principal'),
    path('contato/<int:id>', views.contatoView, name='contato'),
]