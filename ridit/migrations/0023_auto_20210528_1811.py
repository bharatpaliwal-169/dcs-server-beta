# Generated by Django 3.2 on 2021-05-28 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridit', '0022_auto_20210526_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='days',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(30)]),
        ),
        migrations.AlterField(
            model_name='school',
            name='vehicle',
            field=models.CharField(choices=[('2w', '2 wheeler'), ('3w', '3 wheeler'), ('4w', '4 wheeler'), ('4cw', '4 Wheeler Commercials'), ('hw', 'Heavy Wheeler')], max_length=20),
        ),
    ]
