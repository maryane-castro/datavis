# Generated by Django 3.2.12 on 2023-05-11 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='nome',
            field=models.IntegerField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='valor',
            field=models.FloatField(),
        ),
    ]