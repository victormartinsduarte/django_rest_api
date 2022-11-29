from django.db import models
import datetime


class Imovel(models.Model):
    # id = models.AutoField(primary_key=True)
    limite_hospedes = models.IntegerField(default=1)
    qtd_banheiros = models.IntegerField(default=1)
    aceita_pets = models.BooleanField(default=False)
    limpeza = models.DecimalField(max_digits=6, decimal_places=2, default=70.00)
    data_ativacao = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# python manage.py makemigrations
# python manage.py migrate
# python manage.py loaddata imovel

class Anuncio(models.Model):
    # id = models.AutoField(primary_key=True)
    imovel_anunciando = models.ForeignKey(Imovel, related_name="anuncios", on_delete=models.CASCADE)
    plataforma_anunciante = models.CharField(max_length=50)
    taxa_plataforma = models.DecimalField(max_digits=6, decimal_places=2, default=50.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)