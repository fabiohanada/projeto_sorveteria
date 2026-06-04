from django.contrib import admin
from .models import Embalagem, TipoSabor, Sabor, Cobertura, MontaPote, SelSabor, SacolaItens, Pedido

# Register your models here.
admin.site.register(Embalagem)
admin.site.register(TipoSabor)
admin.site.register(Sabor)
admin.site.register(Cobertura)


# Monta Pote - Adiciona os sabores ao modelo MontaPote usando TabularInline
class SelSaborInline(admin.TabularInline):
    model = SelSabor
    extra = 0  # Número de formulários vazios adicionais para adição de novos itens

@admin.register(MontaPote)
class MontaPoteAdmin(admin.ModelAdmin):
    inlines = [SelSaborInline]  # Inclui os sabores diretamente na visualização de MontaPote

class MontaPoteInline(admin.TabularInline):
    model = SacolaItens.potes.through  # Relacionamento muitos-para-muitos entre MontaPote e SacolaItens
    extra = 0  # Número de formulários vazios adicionais
    
class PedidoInline(admin.StackedInline):
    model = Pedido
    extra = 0  # Número de formulários vazios adicionais

@admin.register(SacolaItens)
class SacolaItensAdmin(admin.ModelAdmin):
    fields = ('preco',)  # Campos a serem exibidos no modelo SacolaItens
    readonly_fields = ('preco',)  # O campo preço será somente leitura
    inlines = [PedidoInline, MontaPoteInline]  # Adiciona os inlines para Pedido e MontaPote
