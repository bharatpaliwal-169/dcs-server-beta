# Generated by Django 3.2.3 on 2021-06-21 10:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ridit', '0033_alter_school_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chauffer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='id',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='id',
        ),
        migrations.RemoveField(
            model_name='puc',
            name='id',
        ),
        migrations.RemoveField(
            model_name='school',
            name='id',
        ),
        migrations.AddField(
            model_name='chauffer',
            name='eid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='insurance',
            name='eid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='partner',
            name='eid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='puc',
            name='eid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='school',
            name='eid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='chauffer',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Only Alphabets are allowed', regex='^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Only Alphabets are allowed', regex='^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='partner',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Only Alphabets are allowed', regex='^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='puc',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Only Alphabets are allowed', regex='^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='school',
            name='days',
            field=models.CharField(choices=[('0', '7 days'), ('1', '15 days')], max_length=10),
        ),
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Only Alphabets are allowed', regex='^[A-Za-z]*$')]),
        ),
        migrations.AlterField(
            model_name='school',
            name='vehicle',
            field=models.CharField(choices=[('2w', '2 wheeler'), ('3w', '3 wheeler'), ('4w', '4 wheeler'), ('hw', 'Heavy Wheeler')], max_length=20),
        ),
        migrations.CreateModel(
            name='Rto',
            fields=[
                ('eid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message='Only Alphabets are allowed', regex='^[A-Za-z]*$')])),
                ('contact', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be of 10 digits', regex='^\\+?1?\\d{10}$')])),
                ('serv', models.CharField(choices=[('0', 'Transfer'), ('1', 'Fitness'), ('2', 'DL'), ('3', 'NOC'), ('4', 'RC Removal'), ('5', 'Others')], max_length=60)),
                ('others', models.TextField(max_length=300)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ridit.city')),
            ],
        ),
    ]