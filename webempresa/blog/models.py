from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(verbose_name = 'Nombre', max_length=100)
    created = models.DateTimeField(verbose_name = 'Fecha Creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha Actualización', auto_now = True)

    class Meta:
        verbose_name = "categoría"
        verbose_name_plural = "categorías"
        ordering = ["-created"]

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(verbose_name = 'Título', max_length=200)
    content = models.TextField(verbose_name = 'Contenido',)
    published = models.DateTimeField(verbose_name = 'Fecha Publicación', default = now)
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name = 'Autor', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name = 'Categorías', related_name='get_posts')
    created = models.DateTimeField(verbose_name = 'Fecha Creación', auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Fecha Actualización', auto_now = True)

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title