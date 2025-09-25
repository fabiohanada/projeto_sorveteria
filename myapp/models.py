from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# tipo de pote
class Embalagem(models.Model):
    tipo = models.CharField(max_length=50)
    capacidade = models.DecimalField(max_digits=10, decimal_places=2) 
    ativo = models.BooleanField(default=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def preco_formatado(self):
        return f"R$ {self.preco:.2f}"
    
    def __str__(self):
        return f"{self.tipo} | PREÇO: R$ {self.preco:.2f}"
    
    class Meta:
        verbose_name = '1 - Embalagem'
        verbose_name_plural = '1 - Embalagens'
        
# sabor do sorvete
class TipoSabor(models.Model):
    tipo = models.CharField(max_length=100)
    ativo = models.BooleanField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    
    def preco_formatado(self):
        return f'R$ {self.preco:.2f}'
    
    def __str__(self):
        return f'{self.tipo} | PREÇO: R$ {self.preco:.2f}'
    
    class Meta:
        verbose_name = '2 - TipoSabor'
        verbose_name_plural = '2 - TipoSabor'
        
#lista de sabores escolhidos
class Sabor(models.Model):
    nome = models.CharField(max_length=50, default='Sabor generico')
    tipo = models.ForeignKey(TipoSabor, 
                             related_name='tipo_sabor',
                             on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.nome} | PREÇO: R$ {self.tipo.preco:.2f}'
    
    class Meta:
        verbose_name = '3 - Sabor'
        verbose_name_plural = '3 - Sabor'
        
# Coberturas Disponíveis
class Cobertura(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField()
    
    def preco_formatado(self):
        return f'R$ {self.preco:.2f}'
    
    def __str__(self):
        return f'{self.nome} | PREÇO: R$ {self.preco:.2f}'
    
    class Meta:
        verbose_name = '4 - Cobertura'
        verbose_name_plural = '4 - Cobertura'
        
# Monta o pote
class MontaPote(models.Model):
    embalagem = models.ForeignKey(Embalagem, related_name='embalagem', on_delete=models.CASCADE)
    coberturas = models.ManyToManyField(Cobertura)
    quantidade = models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f"ID: {self.id} / POTE: {self.embalagem.tipo} \
            / Qtd: {self.quantidade} / {self.preco_total()}"

    class Meta:
        verbose_name = 'B - MontaPote'
        verbose_name_plural = 'B - MontaPote'