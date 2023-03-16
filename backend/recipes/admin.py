from django.contrib.admin import ModelAdmin, register

from .models import Cart, Favorite, Ingredient, IngredientAmount, Recipe, Tag


@register(Tag)
class TagAdmin(ModelAdmin):
    list_display = ('name', 'slug', 'color')


@register(Ingredient)
class IngredientAdmin(ModelAdmin):
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)
    search_fields = ('name',)


@register(Recipe)
class RecipeAdmin(ModelAdmin):
    list_display = ('name', 'author')
    list_filter = ('author', 'name', 'tags')
    readonly_fields = ('count_favorites',)
    search_fields = ('name',)

    def count_favorites(self, obj):
        return obj.favorites.count()

    count_favorites.short_description = 'Число добавлений в избранное'


@register(IngredientAmount)
class IngredientAmountAdmin(ModelAdmin):
    list_display = ('recipe',)
    search_fields = ('recipe',)


@register(Favorite)
class FavoriteAdmin(ModelAdmin):
    list_display = ('recipe', 'user')
    search_fields = ('recipe', 'user') 


@register(Cart)
class CartAdmin(ModelAdmin):
    list_display = ('recipe',)
    search_fields = ('recipe',)
    