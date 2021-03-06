from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Ocultar"),
    (1,"Publicar")
)

class Categoria(models.Model):
    categoria = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    producto = models.CharField(max_length=200, unique=True) 
    imagen=  models.ImageField(blank=True)
    categoria = models.ForeignKey(Categoria, verbose_name="Category", on_delete = models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    descripcion = models.CharField(max_length=200)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    status = models.IntegerField(choices=STATUS, default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.producto

PEDIDO = (
    (0,"ENVIADO"),
    (1,"PROCESANDO"),
    (2,"ENTREGADO")
)

class Pedido(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=128)
    referencia = models.CharField(max_length=200)
    telefono= models.CharField(max_length=8)
    productos =models.ManyToManyField(Producto)
    estado = models.IntegerField(choices=PEDIDO, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    def productos_pedido(self):
        return "\n".join([p.producto for p in self.productos.all()])

