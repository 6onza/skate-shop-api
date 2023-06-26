from django.db import models
from cloudinary.models import CloudinaryField

CATEGORIES = (
    ('tablas', 'Tablas'),
    ('ruedas', 'Ruedas'),
    ('trucks', 'Trucks'),
    ('lijas', 'Lijas'),
    ('rulemanes', 'Rulemanes'),
    ('skate-completo', 'Skate completo'),
    ('llaves', 'Llaves'),
    ('remeras', 'Remeras'),
    ('buzos', 'Buzos'),
    ('camperas', 'Camperas'),
    ('gorras', 'Gorras'),
    ('zapatillas', 'Zapatillas'),
    ('accesorios', 'Accesorios'),
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True, null=True, default='')
    description = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORIES, default='tablas')
    size = models.ManyToManyField('Size', blank=True, related_name='products')
    image_1 = CloudinaryField('image_1', blank=True, null=False)
    image_2 = CloudinaryField('image_2', blank=True, null=False)
    image_3 = CloudinaryField('image_3', blank=True, null=False)

    def __str__(self):
        return self.name

    def get_sizes(self):
        return "\n".join([p.name for p in self.size.all()])
    get_sizes.short_description = 'Talles'




class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
