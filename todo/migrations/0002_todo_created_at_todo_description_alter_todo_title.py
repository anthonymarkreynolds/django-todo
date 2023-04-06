# Generated by Django 4.2 on 2023-04-06 00:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(default='no description', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
