# Generated by Django 2.0.4 on 2018-04-23 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20180423_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-id']},
        ),
    ]
