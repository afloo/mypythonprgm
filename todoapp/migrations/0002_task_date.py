# Generated by Django 4.2.4 on 2023-09-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2003-01-12'),
            preserve_default=False,
        ),
    ]
