# Generated by Django 4.2.11 on 2024-04-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('qualification', models.CharField(max_length=255)),
                ('experience', models.PositiveIntegerField()),
                ('available_from', models.TimeField()),
                ('available_to', models.TimeField()),
            ],
        ),
    ]
