from rest_framework import serializers

from .models import Imovel

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
