from django.contrib import admin
from .models import Embalagem, TipoSabor, Sabor, Cobertura

# Register your models here.
admin.site.register(Embalagem)
admin.site.register(TipoSabor)
admin.site.register(Sabor)
admin.site.register(Cobertura)