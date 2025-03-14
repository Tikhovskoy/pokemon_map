from django.db import models

class Pokemon(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название покемона")
    title_en = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название (англ.)")
    title_jp = models.CharField(max_length=200, null=True, blank=True, verbose_name="Название (яп.)")
    image = models.ImageField(upload_to='pokemons/', null=True, blank=True, verbose_name="Изображение")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

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

    level = models.IntegerField(default=1, verbose_name="Уровень")
    health = models.IntegerField(default=100, verbose_name="Здоровье")
    attack = models.IntegerField(default=10, verbose_name="Атака")
    defense = models.IntegerField(default=5, verbose_name="Защита")
    stamina = models.IntegerField(default=50, verbose_name="Выносливость")
    
    def __str__(self):
        return f"{self.pokemon.title} (Lvl {self.level}, {round(self.latitude, 5)}, {round(self.longitude, 5)})"