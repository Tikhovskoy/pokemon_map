from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название покемона")
    image = models.ImageField(upload_to='pokemons/', null=True, blank=True, verbose_name="Изображение")

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name="entities",
        verbose_name="Покемон"
    )
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Появился в")
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Исчез в")

    def __str__(self):
        return f"{self.pokemon.title} ({round(self.latitude, 5)}, {round(self.longitude, 5)})"
