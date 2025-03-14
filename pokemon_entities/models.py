from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название (рус.)")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Название (англ.)")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="Название (яп.)")
    image = models.ImageField(upload_to='pokemons/', blank=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    previous_evolution = models.ForeignKey(
        "self",
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="next_evolutions",
        verbose_name="Из кого эволюционировал"
    )

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

    level = models.PositiveIntegerField(null=True, blank=True, verbose_name="Уровень")
    health = models.PositiveIntegerField(null=True, blank=True, verbose_name="Здоровье")
    attack = models.PositiveIntegerField(null=True, blank=True, verbose_name="Атака")
    defense = models.PositiveIntegerField(null=True, blank=True, verbose_name="Защита")
    stamina = models.PositiveIntegerField(null=True, blank=True, verbose_name="Выносливость")

    def __str__(self):
        return f"{self.pokemon.title} (Lvl {self.level if self.level else '??'}, {round(self.latitude, 5)}, {round(self.longitude, 5)})"
