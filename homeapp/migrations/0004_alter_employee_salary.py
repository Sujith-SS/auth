# Generated by Django 5.0.6 on 2024-06-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0003_department_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
