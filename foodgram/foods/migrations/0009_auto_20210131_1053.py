# Generated by Django 3.0.8 on 2021-01-31 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0008_auto_20210130_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тэг', 'verbose_name_plural': 'тэги'},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='style',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='value',
        ),
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=10, null=True, verbose_name='Цвет тега'),
        ),
        migrations.AddField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=20, null=True, verbose_name='Отображаемно название'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20, null=True, verbose_name='Имя тега'),
        ),
    ]
