from django.shortcuts import render
from django.views import generic
from .models import * 

class ProdList(generic.ListView):
    queryset = Producto.objects.filter(status=1,).order_by('-created_on')
    template_name = 'index.html'

class ProdDetail(generic.DetailView):
    model = Producto
    template_name = 'prod_detail.html'