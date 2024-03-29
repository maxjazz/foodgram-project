# Generated by Django 3.0.8 on 2021-02-08 12:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0009_auto_20210131_1053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'verbose_name': 'избранное', 'verbose_name_plural': 'избранное'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ('name',), 'verbose_name': 'ингредиент', 'verbose_name_plural': 'ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'ordering': ('user',), 'verbose_name': 'список покупок', 'verbose_name_plural': 'список покупок'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'подписка', 'verbose_name_plural': 'подписки'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('name',), 'verbose_name': 'тэг', 'verbose_name_plural': 'тэги'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название ингредиента'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=10, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='quantity',
            field=models.DecimalField(decimal_places=0, max_digits=6, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=20, null=True, verbose_name='Отображаемое название'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
