from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class User(AbstractUser):

    class Role(models.TextChoices):
        ANONYM = 'anonym', _('Anonym')
        USER = 'user', _('User')
        ADMIN = 'admin', _('Admin')

    email = models.EmailField(_('email address'), blank=False, unique=True)
    bio = models.TextField(blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.USER,
        )
    confirmation_code = models.CharField(max_length=100, blank=True, )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Tag(models.Model):
    title = models.CharField('Отображаемно название', max_length=20, null=True)
    color = models.CharField('Цвет тега', max_length=10, null=True)
    name = models.CharField('Имя тега', max_length=20, null=True)

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Stores a single Recipe entry. Related to `auth.User` , `recipes.Tag` and
    `recipes.Ingredient` through intermediate model `recipes.RecipeIngredient`.
    """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    title = models.CharField('Название рецепта', max_length=200)
    image = models.ImageField('Изображение', upload_to='recipes/')
    text = models.TextField('Текст рецепта')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиент'
    )
    cooking_time = models.PositiveSmallIntegerField('Время приготовления')
    tags = models.ManyToManyField(
        'Tag',
        related_name='recipes',
        verbose_name='Теги'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    """
    Intermediate model that supports a Many-to-Many relationship between
    `recipes.Recipe` and `recipes.Ingredient`.
    Also stores an additional `quantity` field.
    """
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredient'
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=0,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = ('ingredient', 'recipe')


class Favorite(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE,
        related_name='favorite_recipes',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorites"
    )

    def __str__(self):
        return self.recipe.title


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following"
    )

    def __str__(self):
        return self.user.username

    def follower(self):
        return self.user.username

    def following(self):
        return self.author.username


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="shopping_list"
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_list'
    )

    def __str__(self):
        return self.recipe.title
