# Generated by Django 4.1.2 on 2022-10-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]