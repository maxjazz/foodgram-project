from django.contrib import admin
from .models import Ingredient, User, Recipe, Tag, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    min_num = 1
    extra = 0
    verbose_name = 'Ингредиенты'


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'unit')
    list_filter = ('name',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')
    list_filter = ('email', 'first_name',)


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline,)
    list_display = ('title', 'text')
    list_filter = ('title',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'color')


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'recipe', 'quantity')


admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
