# Generated by Django 3.2.5 on 2022-09-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMedule', '0008_auto_20220901_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priroty',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='color'),
        ),
    ]