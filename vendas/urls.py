from django.urls import path
from . import views

urlpatterns = [
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/novo/', views.criar_venda, name='criar_venda'),
    path('vendas/editar/<int:id>/', views.editar_venda, name='editar_venda'),
    path('vendas/excluir/<int:id>/', views.excluir_venda, name='excluir_venda'),
]
