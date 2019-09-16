from django.urls import path
from . import views

app_name = 'busca'
urlpatterns = [
    path('busca/<int:contato_id>', views.contatoView, name='busca'),
    path('addcontato/', views.addcontato, name='add-contato'),
    path('edit/<int:contato_id>', views.editcontato, name='edit-contato'),
    path('', views.page_principal, name='principal'),
]