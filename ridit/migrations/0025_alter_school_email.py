# Generated by Django 3.2 on 2021-05-28 15:37

from django.db import migrations, models
import ridit.models


class Migration(migrations.Migration):

    dependencies = [
        ('ridit', '0024_alter_school_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='email',
            field=models.EmailField(max_length=200, validators=[ridit.models.validateEmail]),
        ),
    ]
