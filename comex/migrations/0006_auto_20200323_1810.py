# Generated by Django 2.2.11 on 2020-03-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comex', '0005_auto_20200323_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='description',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='network',
            name='managed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='network',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='network',
            name='networkType',
            field=models.CharField(default='Bridged', max_length=30),
        ),
        migrations.AlterField(
            model_name='network',
            name='status',
            field=models.CharField(default='Created', max_length=30),
        ),
    ]
