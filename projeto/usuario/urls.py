from django.urls import path, include
from .views import usuario_detail,usuario_list_create,home_page,list_page



urlpatterns = [
    path('',home_page,name='home'),
    path('usuarios/',list_page,name='list_page'),
    path('api/usuarios/', usuario_list_create,name='usuario_list_create'),
    path('api/usuarios/<int:pk>/',usuario_detail,name='usuario-detail'),
]