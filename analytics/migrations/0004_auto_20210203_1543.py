# Generated by Django 3.0.3 on 2021-02-03 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_remove_objectlead_click_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectlead',
            name='ip_address',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
