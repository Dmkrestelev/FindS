# Generated by Django 2.0.4 on 2018-04-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hlam', '0004_auto_20180423_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='sex',
            field=models.CharField(max_length=30, null=True),
        ),
    ]