# Generated by Django 4.2.11 on 2024-08-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeraccounts',
            name='date',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='otheraccounts',
            name='date',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]