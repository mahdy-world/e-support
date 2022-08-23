# Generated by Django 3.2.5 on 2022-08-23 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0013_remove_issue_last_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Train Name')),
                ('t_from', models.CharField(blank=True, max_length=50, null=True, verbose_name='From')),
                ('t_to', models.CharField(blank=True, max_length=50, null=True, verbose_name='To')),
                ('number', models.IntegerField(verbose_name='Train Number')),
            ],
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='create',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='last_update',
            new_name='update_date',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='field',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='folder_id',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='screen',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='supscription_type',
        ),
        migrations.AddField(
            model_name='issue',
            name='follwer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='issue_follwer', to=settings.AUTH_USER_MODEL, verbose_name='Follwer'),
        ),
        migrations.AddField(
            model_name='issue',
            name='teller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.enruser', verbose_name='Teller'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='jira_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Jira Id'),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Subscription Type')),
                ('number', models.IntegerField()),
                ('expiry_date', models.DateField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.issue', verbose_name='Issue')),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='train',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.train', verbose_name='Train'),
        ),
    ]
