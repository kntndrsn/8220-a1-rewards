# Generated by Django 3.1.5 on 2021-01-20 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rewardsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Description'),
        ),
    ]
