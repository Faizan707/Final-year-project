# Generated by Django 4.2.11 on 2024-04-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_rename_student_name_duefee_customer_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duefee',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], max_length=20),
        ),
    ]