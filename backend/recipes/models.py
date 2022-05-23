from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Название', 
        max_length=200,  
        help_text='О названии тэгов',
        unique=True,
    )
    color = models.CharField(
        verbose_name='Цвет в HEX', 
        max_length=7, unique=True,
        help_text='Цвета тэгов',
    )
    slug = models.SlugField(
        verbose_name='Уникальный слаг', 
        max_length=200, unique=True,
        help_text='Слаг тэга',
    )
    

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ('-id',)

    def __str__(self) -> str:
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название', 
        max_length=200,
        help_text='О названии ингридиентов',
    )
    measurement_unit = models.CharField(
        verbose_name='Единицы измерения', 
        max_length=20,
        help_text='Сколько надо ингридиентов',
    )
    

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'
        ordering = ('name',)
        constraints = [ 
            models.UniqueConstraint(fields=['name', 'measurement_unit'], 
                                    name='unique_for_ingredient')] 

    def __str__(self) -> str:
        return f'{self.name}'


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор публикации',
        related_name='recipes',
        help_text='Хозяин рецепта',
    )
    name = models.CharField(
        verbose_name='Название', 
        max_length=200,
        help_text='Название рецепта',
    )
    image = models.ImageField(
        verbose_name='Картинка', 
        upload_to='recipe_images/',
        help_text='Картинка рецепта',
    )
    text = models.TextField(
        verbose_name='Текстовое описание',
        help_text='Описание рецепта',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='recipes.IngredientAmount',
        verbose_name='Ингредиенты',
        related_name='recipes',
        help_text='Ингридиенты для рецепта',
    )
    tags = models.ManyToManyField(
        Tag, verbose_name='Тег', related_name='recipes')
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления в минутах',
        validators=[validators.MinValueValidator(
            1, message='Минимальное время приготовления 1 минута'),
        ]
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ('-pub_date', )

    def __str__(self) -> str:
        return f'{self.name}'


class IngredientAmount(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='В каких рецептах',
        related_name='ingredient',
        help_text='В каких рецептах',
    )
    ingredients = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Связанные ингредиенты',
        related_name='recipe',
        help_text='Связанные ингридиенты',
    )
    amount = models.PositiveSmallIntegerField(
        default=1,
        validators=(
            validators.MinValueValidator(
                1, message='Минимальное количество ингридиентов 1'),),
        verbose_name='Количество',
    )
    

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Количество ингридиента'
        verbose_name_plural = 'Количество ингридиентов'
        constraints = [ 
            models.UniqueConstraint(fields=['recipe', 'ingredients'], 
                                    name='unique_ingredients_recipe') 
        ] 

    def __str__(self) -> str:
        return f'{self.ingredients.name} - {self.amount}'


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Пользователь',
        help_text='Корзина пользователя',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Рецепт',
        help_text='Рецепт',
    )
    

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Корзина'
        verbose_name_plural = 'В корзине'
        constraints = [ 
            models.UniqueConstraint(fields=['user', 'recipe'], 
                                    name='unique_cart_user') 
        ] 


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='favorites',
        help_text='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Рецепт',
        help_text='Рецепт',
    )
    

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        constraints = [ 
            models.UniqueConstraint(fields=['user', 'recipe'], 
                                    name='unique_user_recipe') 
        ] 

    def __str__(self):
        return f'{self.user}'