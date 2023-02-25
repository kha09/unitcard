# Generated by Django 4.0.6 on 2023-02-25 15:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('website', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filecard', models.FileField(upload_to='card/')),
                ('imgcard', models.ImageField(default='img01.png', upload_to='img/')),
            ],
        ),
    ]
