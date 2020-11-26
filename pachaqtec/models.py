from django.db import models

# Create your models here.

class Tipo_Imagen(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion
    
    #class Meta():
    #    verbose_name = 'Tipo Imagen'
    #    verbose_name_plural = 'Tipos de Imagen'

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    descripcion_producto = models.TextField()
    descripcion_corta = models.TextField()
    descripcion_larga = models.TextField()
    precio = models.DecimalField(decimal_places=2)
    telefono = models.CharField(max_length=20)
    orientado_a = models.TextField()
    otorga = models.TextField()

    def __str__(self):
        return self.descripcion_producto

class Imagen_Producto(models.Model):
    imagen_producto_id = models.AutoField(primary_key=True)
    tipo_imagen = models.ForeignKey(Tipo_Imagen, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)

    def __str__(self):
        return self.nombre

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    estado_pago = models.BooleanField()
    total = models.DecimalField(decimal_places=2)
    moneda = models.CharField(max_length=3)
    estado = models.BooleanField()

    def __str__(self):
        return self.customer_id

class Orders_detail(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    posicion = models.DateField()
    producto_id = models.CharField()
    descripcion = models.TextField()
    cantidad = models.CharField()
    importe = models.DecimalField(decimal_places=2)

    def __str__(self):
        return self.descripcion

class Carrito(models.Model):
    carrito_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    total = models.DecimalField(decimal_places=2)
    moneda = models.CharField(max_length=3)
    descuento_id = models.DecimalField(decimal_places=2)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion