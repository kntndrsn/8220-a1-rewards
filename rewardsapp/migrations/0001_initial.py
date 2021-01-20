# Generated by Django 3.1.5 on 2021-01-20 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, verbose_name='Employee Number')),
                ('firstname', models.CharField(max_length=20, verbose_name='First Name')),
                ('lastname', models.CharField(max_length=20, verbose_name='Last Name')),
                ('active', models.BooleanField(verbose_name='Employee Active')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('description', models.CharField(max_length=20, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awarded_on', models.DateField(default=django.utils.timezone.now, verbose_name='Awarded On')),
                ('awarded_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Awarded By')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='rewardsapp.employee', verbose_name='Employee')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward', to='rewardsapp.reward', verbose_name='Reward')),
            ],
        ),
    ]
