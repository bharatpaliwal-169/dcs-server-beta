# Generated by Django 3.2 on 2021-05-21 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ridit', '0014_auto_20210521_1739'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chauffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('contact', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be of 10 digits', regex='^\\+?1?\\d{10}$')])),
                ('address', models.CharField(max_length=400)),
                ('date', models.DateField()),
                ('pincode', models.CharField(max_length=6)),
                ('days', models.IntegerField()),
            ],
        ),
    ]
