# Generated by Django 2.0.7 on 2019-01-21 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtask',
            name='content',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.CharField(max_length=300),
        ),
    ]
