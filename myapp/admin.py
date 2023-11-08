from django.contrib import admin
from .models import Descricoes
from .models import Diaria
from .models import Usuario

admin.site.register(Descricoes)

admin.site.register(Usuario)

class DiariaAdmin(admin.ModelAdmin):
    fields = ['dia', 'disponibilidade', 'preco', 'hospede']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "hospede":
            kwargs["required"] = False
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Diaria, DiariaAdmin)