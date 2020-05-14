from django.contrib import admin
from .models import * 

admin.site.site_header = 'El Globo Admin Dashboard'

class CategAdmin (admin.ModelAdmin):
    list_display = ('categoria',)
    search_fields = ['categoria']
    list_filter = ("categoria",)
admin.site.register(Categoria, CategAdmin)


class ProdAdmin(admin.ModelAdmin):
    list_display = ('producto', 'categoria', 'price','descripcion')
    list_filter = ('categoria',)
    search_fields = ['producto','slug']
    prepopulated_fields = {'slug': ('producto',)}

admin.site.register(Producto, ProdAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion','referencia','telefono','productos_pedido','estado','created_on','updated_on')
    list_filter = ("estado",)
    search_fields = ['nombre',]
  
admin.site.register(Pedido, PedidoAdmin)

