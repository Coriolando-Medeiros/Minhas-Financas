from django.db import models


class Category(models.Model):
    RECEITA = 'receita'
    DESPESA = 'despesa'

    TIPO_CHOICES = [
        (RECEITA, 'Receita'),
        (DESPESA, 'Despesa'),
    ]

    name = models.TextField(max_length=100)
    type_category = models.CharField(max_length=20, choices=TIPO_CHOICES)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)
