from django.contrib import admin
from .models import Atendimento, MaterialUtilizado


class MaterialInline(admin.TabularInline):
    model = MaterialUtilizado
    extra = 1


@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "data", "tecnico", "status")
    list_filter = ("status", "data")
    search_fields = ("cliente", "descricao")
    inlines = [MaterialInline]


@admin.register(MaterialUtilizado)
class MaterialAdmin(admin.ModelAdmin):
    list_display = (
        "nome_material",
        "atendimento",
        "quantidade_utilizada",
        "quantidade_danificada",
    )