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

# python manage.py makemigrations (faz com que o db saiba o que as models existem)
# python manage.py migrate (faz o db mudar conforme as models)
# python manage.py loaddata imovel