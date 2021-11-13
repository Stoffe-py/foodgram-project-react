from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

#Модель для ингридиентов
class Ingredient(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя ингредиента')
    measurement_unit = models.CharField(max_length=50, verbose_name='Ед. измерения')

    def __str__(self):
        return self.name


#Модель тегов
class Tag(models.Model):
    #Коды цветов
    RED = '#FF0000'
    GREEN = '#006400'
    BLUE = '#0000FF'
    BROWN = '#A52A2A'
    PURPLE = '#800080'

    #Чойсы
    CHOICES = [
        (RED, 'Красный'),
        (GREEN, 'Зеленый'),
        (BLUE, 'Синий'),
        (BROWN, 'Коричневый'),
        (PURPLE, 'Фиолетовый'),
    ]

    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Имя тега')
    color = models.CharField(max_length=30, unique=True, choices=CHOICES,
                             verbose_name='HEX-цвет')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='Слаг')

    def __str__(self):
        return self.name

#Модель рецептов
class Recept(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recept',
                               verbose_name='Автор рецепта')
    name = models.CharField(max_length=150, verbose_name='Имя рецепта')
    image = models.ImageField(upload_to='images/', verbose_name='Картинка')
    text = models.CharField(max_length=500, verbose_name='Описание')
    ingredients = models.ManyToManyField(Ingredient,
                                         verbose_name='Ингредиенты')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    cooking_time = models.PositiveSmallIntegerField(verbose_name='Время готовки')

#Всп. модель для кол-ва
class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                   verbose_name='Ингридиент')
    recipe = models.ForeignKey(Recept, on_delete=models.CASCADE,
                               verbose_name='Рецепт')
    amount = models.PositiveSmallIntegerField(verbose_name='Количество')

#Избранное
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                            verbose_name='Пользователь')
    recipe = models.ForeignKey(Recept, on_delete=models.CASCADE,
                               related_name='favorites',
                               verbose_name='Рецепт')


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                            related_name='cart', verbose_name='Пользователь')
    recipe = models.ForeignKey(Recept, on_delete=models.CASCADE,
                               related_name='cart', verbose_name='Рецепт')
