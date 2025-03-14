from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название покемона")
    image = models.ImageField(upload_to='pokemons/', null=True, blank=True, verbose_name="Изображение")
    def __str__(self):
        return self.title
