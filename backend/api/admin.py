from django.contrib import admin

from .models import Cart, Favorite, IngredientAmount, Tag, Ingredient, Recept


admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Recept)
admin.site.register(IngredientAmount)
admin.site.register(Cart)
admin.site.register(Favorite)