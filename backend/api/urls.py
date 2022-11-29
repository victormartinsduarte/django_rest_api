from django.urls import path

from . import views


urlpatterns = [
    path('imoveis/', views.imoveis_list_create_view),
]