# Generated by Django 3.2.5 on 2021-07-21 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0002_auto_20210721_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='service',
            name='remark',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ремарки'),
        ),
    ]