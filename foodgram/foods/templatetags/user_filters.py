from django import template

from ..models import Favorite, ShoppingList

register = template.Library()


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.filter(name="is_favorite")
def is_favorite(request, recipe):
    if Favorite.objects.filter(
            user=request.user, recipe=recipe
    ).exists():
        return True
    return False


@register.filter(name="in_shoplist")
def in_shoplist(request, recipe):
    if ShoppingList.objects.filter(
            user=request.user, recipe=recipe
    ).exists():
        return True
    return False


@register.filter(name="is_checked")
def is_checked(tag, available_tags):
    if not available_tags:
        return False
    if tag in [int(i) for i in available_tags]:
        return True
    return False


@register.filter(name="recipe_name")
def recipe_name(num):
    if 10 < num < 21:
        return 'рецептов'
    if num % 10 == 1:
        return 'рецепт'
    if num % 10 in [2, 3, 4]:
        return 'рецепта'
    return 'рецептов'
