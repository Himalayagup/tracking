# Generated by Django 3.0.3 on 2021-05-20 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0007_auto_20210520_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='objectlead',
            name='click_id',
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='objectviewed',
            name='click_id',
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
    ]
