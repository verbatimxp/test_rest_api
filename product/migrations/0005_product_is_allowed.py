# Generated by Django 3.0.6 on 2020-05-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200513_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_allowed',
            field=models.BooleanField(default=True),
        ),
    ]
