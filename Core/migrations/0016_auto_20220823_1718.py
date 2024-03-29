# Generated by Django 3.2.5 on 2022-08-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0015_auto_20220823_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='teller_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Teller Name'),
        ),
        migrations.AddField(
            model_name='issue',
            name='teller_phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Teller phone'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='subscription_expiry_date',
            field=models.DateField(blank=True, null=True, verbose_name='Subscription Expiry Date'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='subscription_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Subscription Number'),
        ),
    ]
