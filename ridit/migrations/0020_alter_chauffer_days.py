# Generated by Django 3.2 on 2021-05-26 11:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridit', '0019_auto_20210526_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chauffer',
            name='days',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30, message='wrong')]),
        ),
    ]
