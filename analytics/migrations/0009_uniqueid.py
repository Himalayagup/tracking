# Generated by Django 3.0.3 on 2021-05-20 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0008_auto_20210520_1918'),
    ]

    operations = [
        migrations.CreateModel(
            name='UniqueID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.UUIDField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
