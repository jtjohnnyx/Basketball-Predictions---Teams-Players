# Generated by Django 4.2 on 2023-04-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestats', '0003_teamcache_delete_api'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='city',
        ),
        migrations.RemoveField(
            model_name='team',
            name='code',
        ),
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.RemoveField(
            model_name='team',
            name='nick',
        ),
        migrations.RemoveField(
            model_name='teamcache',
            name='info',
        ),
        migrations.AddField(
            model_name='teamcache',
            name='city',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamcache',
            name='code',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teamcache',
            name='nick',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teamcache',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
