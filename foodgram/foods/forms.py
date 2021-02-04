from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'cooking_time',
            'text',
            'image',
            'tags',
        )
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
