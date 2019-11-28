from django.db import models


class People(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='Email')
    telefone = models.CharField(verbose_name='Telefone', max_length=20)

    def __str__(self):
        return self.name + ' - ' + self.email
