# Generated by Django 3.2.5 on 2022-08-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMedule', '0006_auto_20220818_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='arabic_name',
            field=models.CharField(max_length=100, verbose_name='Station'),
        ),
    ]
