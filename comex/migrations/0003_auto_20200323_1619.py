# Generated by Django 2.2.11 on 2020-03-23 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comex', '0002_auto_20200323_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkconfig',
            name='bridgeMode',
            field=models.CharField(default='wow', max_length=30),
        ),
    ]