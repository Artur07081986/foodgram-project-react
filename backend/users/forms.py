from django.forms.models import BaseInlineFormSet
from django.forms import ValidationError


class IngredientAmountFormset(BaseInlineFormSet):
    def clean(self):
        # Если в админке удалить форму для ингредиентов
        if self.forms == []:
            raise ValidationError('Добавьте минимум один ингредиент')
        # Если форма есть, но данные пустые
        if self.cleaned_data == [{}]:
            raise ValidationError('Заполните данные ингредиентов')