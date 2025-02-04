# Generated by Django 3.0.3 on 2021-02-02 10:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_name', models.CharField(help_text='Enter the agency name', max_length=200, verbose_name='Agency Name')),
                ('agency_address', models.CharField(help_text="Enter the agency's address/city", max_length=300, verbose_name="Agency's Address/City")),
                ('contact_person', models.CharField(help_text="Enter the agency's contact person's name", max_length=150, verbose_name="Contact Person's Name")),
                ('email', models.EmailField(help_text="Enter the agency/contact person's mail id", max_length=400, verbose_name="Agency/Contact Person's Mail ID")),
                ('contact_number', models.PositiveIntegerField(help_text="Enter the agency's contact number", validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name="Agency's Contact Number")),
                ('alternate_number', models.PositiveIntegerField(blank=True, help_text="Enter the agency's alternate number", null=True, validators=[django.core.validators.MaxValueValidator(9999999999)], verbose_name='Alternate Contact Number')),
            ],
        ),
    ]
