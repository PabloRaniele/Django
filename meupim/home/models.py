from django.db import models

class Uf(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    sigla = models.ForeignKey(Uf, on_delete=models.CASCADE,
                              related_name='cidades')
    nome = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

    