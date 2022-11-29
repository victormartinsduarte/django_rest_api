from django.urls import path

from . import views


urlpatterns = [
    path('imoveis/', views.imoveis_list_create_view),
    path('imoveis/<int:pk>/', views.imovel_detail_view),
    path('imoveis/<int:pk>/update/', views.imovel_update_view),
    path('imoveis/<int:pk>/delete/', views.imovel_delete_view),

    path('anuncios/', views.anuncios_list_create_view),
    path('anuncios/<int:pk>/', views.anuncio_detail_view),
    path('anuncios/<int:pk>/update/', views.anuncio_update_view),
]
