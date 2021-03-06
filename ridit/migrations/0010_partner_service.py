# Generated by Django 3.2 on 2021-05-21 08:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ridit', '0009_delete_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be of 10 digits', regex='^\\+?1?\\d{10}$')])),
                ('city', models.CharField(max_length=350)),
                ('query', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ridit.service')),
            ],
        ),
    ]
