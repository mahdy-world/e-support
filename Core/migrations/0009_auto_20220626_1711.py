# Generated by Django 3.2.5 on 2022-06-26 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminMedule', '0004_alter_station_station_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0008_auto_20220620_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Station Name')),
                ('office_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Office Name')),
                ('serial_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Serial Number')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Files'),
        ),
        migrations.AddField(
            model_name='issue',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminMedule.station', verbose_name='Station'),
        ),
        migrations.AddField(
            model_name='issue',
            name='supscription_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Supscription Type'),
        ),
        migrations.AddField(
            model_name='issue',
            name='train',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Train'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='jira_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Jira Id'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reporter'),
        ),
        migrations.AddField(
            model_name='issue',
            name='device_serial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.device', verbose_name='Device Serial'),
        ),
    ]
