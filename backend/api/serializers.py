from rest_framework import serializers

from .models import Imovel, Anuncio, Reserva

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = [
            "id",
            "limite_hospedes",
            "qtd_banheiros",
            "aceita_pets",
            "limpeza",
            "data_ativacao",
            "created_at",
            "updated_at",
        ]

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = [
            "id",
            "imovel_anunciando",
            "plataforma_anunciante",
            "taxa_plataforma",
            "created_at",
            "updated_at",
        ]

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            "id",
            "anuncio_referencia",
            "data_check_in",
            "data_check_out",
            "preco_total",
            "comentario",
            "numero_hospedes",
            "created_at",
            "updated_at",
        ]
