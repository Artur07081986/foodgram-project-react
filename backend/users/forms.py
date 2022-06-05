from django.forms.models import BaseInlineFormSet
from django.forms import ValidationError


class IngredientAmountFormset(BaseInlineFormSet):
    def clean(self):
        
        if self.forms == []:
            raise ValidationError('Добавьте минимум один ингредиент')
        
        if self.cleaned_data == [{}]:
            raise ValidationError('Заполните данные ингредиентов')