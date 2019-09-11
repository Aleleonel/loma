from django.urls import path
from . import views

app_name = 'busca'
urlpatterns = [
    path('busca/<int:contato_id>', views.contatoView, name='busca'),
    path('addcontato/', views.addcontato, name='addcontato'),
    path('', views.page_principal, name='principal'),
]