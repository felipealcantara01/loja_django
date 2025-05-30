from django.contrib import admin
from .models import Venda

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'quantidade', 'data_venda', 'valor_total')
    search_fields = ('cliente__nome', 'produto__nome')
