# Generated by Django 3.2.5 on 2022-06-19 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_rename_issues_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='affects_version',
            field=models.FloatField(null=True, verbose_name='Affects Version'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='channel',
            field=models.IntegerField(choices=[('TOM', 'TOM'), ('TOM-PCM', 'TOM-PCM'), ('OBS', 'OBS'), ('GATES', 'GATES'), ('OLD-TOM', 'OLD-TOM'), ('BLUE ADMIN', 'BLUE ADMIN'), ('NONE', 'NONE')], verbose_name='Channel'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='environment',
            field=models.IntegerField(choices=[('Production', 'Production'), ('UAT', 'UAT'), ('Test', 'Test')], verbose_name='Environment'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='field',
            field=models.CharField(max_length=100, null=True, verbose_name='Field'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='fix_version',
            field=models.FloatField(null=True, verbose_name='Fix Version'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_class',
            field=models.IntegerField(choices=[('Bussines', 'Bussines'), ('Enhancement', 'Enhancement'), ('Function', 'Function'), ('Requirement', 'New Requirement')], verbose_name='Issue Class'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_type',
            field=models.IntegerField(choices=[('Incident', 'Incident'), ('Task', 'Task')], verbose_name='Issue Type'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='jira_id',
            field=models.CharField(max_length=150, verbose_name='Jira Id'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='last_comment',
            field=models.TextField(null=True, verbose_name='Last Comment'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.IntegerField(choices=[('Critical', 'Critical'), ('Major', 'Major'), ('Minor', 'Minor')], verbose_name='Priority'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='screen',
            field=models.CharField(max_length=100, null=True, verbose_name='Screen'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.IntegerField(choices=[('OPEN', 'OPEN'), ('ClOSED', 'ClOSED'), ('IN PROGRESS', 'IN PROGRESS'), ('RESOLVED', 'RESOLVED')], verbose_name='Status'),
        ),
    ]
