# Generated by Django 4.1.2 on 2023-01-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Emp_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='DOB',
            field=models.DateField(),
        ),
    ]
