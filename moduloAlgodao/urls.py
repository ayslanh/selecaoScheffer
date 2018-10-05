from django.urls import path
from . import views



urlpatterns = [
    path('',views.Index.as_view()),
    path('gestao/',views.gestaoAlgodao.as_view()),
    path('buscarFaz/<int:idFaz>',views.BuscaFazAPIView.as_view(),name='BuscaFaz'),
    path('add_estoque/',views.Estoque.as_view(),name='add_estoque'),
    path('buscaEstoque/<int:idFaz>',views.Estoque.as_view(),name='buscaEstoque'),
]