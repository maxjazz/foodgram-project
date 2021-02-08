from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    def clean(self):
        pass
    
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
