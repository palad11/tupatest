# Generated by Django 3.1.3 on 2020-11-12 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='opros',
            name='opros',
            field=models.ManyToManyField(to='opros.Question'),
        ),
    ]
