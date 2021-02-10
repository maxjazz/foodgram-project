from django import forms
from django.core.exceptions import ValidationError

from .models import Recipe


class RecipeForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        for key in self.data.keys():
            if key.startswith('nameIngredient_'):
                return cleaned_data
        raise ValidationError('Добавьте хотя бы один ингредиент',
                              code='ingredient')

    class Meta:
        model = Recipe
        fields = (
            'title',
            'tags',
            'cooking_time',
            'text',
            'image',
        )
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
