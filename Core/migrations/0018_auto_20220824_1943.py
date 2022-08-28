# Generated by Django 3.2.5 on 2022-08-24 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0017_issue_trans_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='train',
        ),
        migrations.AddField(
            model_name='issue',
            name='train_from',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Train From'),
        ),
        migrations.AddField(
            model_name='issue',
            name='train_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Train Number'),
        ),
        migrations.AddField(
            model_name='issue',
            name='train_to',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Train To'),
        ),
        migrations.DeleteModel(
            name='Train',
        ),
    ]