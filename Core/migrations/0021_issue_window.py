# Generated by Django 3.2.5 on 2022-09-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0020_auto_20220901_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='window',
            field=models.IntegerField(blank=True, choices=[(0, 'W1'), (1, 'W2'), (3, 'W3'), (4, 'W4'), (5, 'W5'), (6, 'W6'), (7, 'W7'), (8, 'W8'), (9, 'W9'), (10, 'W10'), (11, 'W11'), (12, 'W12')], null=True, verbose_name='Windows'),
        ),
    ]