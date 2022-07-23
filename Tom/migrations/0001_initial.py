# Generated by Django 3.2.5 on 2022-07-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant', models.CharField(max_length=50, verbose_name='Merchant')),
                ('terminalId', models.CharField(max_length=50, verbose_name='Terminal Id')),
                ('station', models.IntegerField(verbose_name='Station Id ')),
                ('stationName', models.CharField(max_length=50, verbose_name='Station Name')),
                ('officeName', models.CharField(max_length=50, verbose_name='Office Name')),
            ],
        ),
    ]
