from django.db import models

class Categoria(models.Model):
    nome = models.CharField(verbose_name='Categoria do Produto', blank='flase', null='flase', max_length=200)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        
    def __str__(self):
        return self.nome
