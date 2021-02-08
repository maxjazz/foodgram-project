# Generated by Django 3.0.8 on 2021-02-08 13:44

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0010_auto_20210208_1213'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together={('user', 'recipe')},
        ),
        migrations.AlterUniqueTogether(
            name='shoppinglist',
            unique_together={('user', 'recipe')},
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('user', 'author')},
        ),
    ]