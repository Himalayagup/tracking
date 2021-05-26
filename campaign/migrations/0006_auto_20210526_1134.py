# Generated by Django 3.0.3 on 2021-05-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0005_auto_20210526_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_category',
            field=models.CharField(blank=True, choices=[('banking', 'Banking'), ('matrimony', 'Matrimony'), ('job', 'Job'), ('education', 'Education'), ('finance', 'Finance'), ('insurance', 'Insurance'), ('securities', 'Securities'), ('automobile', 'Automobile'), ('travel_holidays', 'Travel and Holidays'), ('realestate', 'Real Estate'), ('ecommerce', 'E Commerce'), ('classified', 'Classified'), ('recharge_ecommerce', 'Recharge & E Commerce'), ('recharge', 'Recharge'), ('jewellery', 'Jewellery')], help_text='Select the campaing category', max_length=22, null=True, verbose_name='Campaign Category *'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_name',
            field=models.CharField(help_text='Enter the campaign name', max_length=235, verbose_name='Campaign Name *'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='campaign_type',
            field=models.CharField(choices=[('cpl', 'Cost Per Lead'), ('cpc', 'Cost Per Click'), ('cpi', 'Cost Per Impression'), ('cpa', 'Cost Per Action'), ('cpv', 'Cost Per Visit'), ('cps', 'Cost Per Sale'), ('cpinstall', 'Cost Per Install'), ('cpo', 'Cost Per Open'), ('cpsm', 'Cost Per Sent Mailer(s)')], help_text='Select the campaing types', max_length=22, verbose_name='Campaign Type *'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='end_date',
            field=models.DateField(help_text="Enter the campaign's end date (format: YYYY-MM-DD)", verbose_name='End Date *'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='expire_url',
            field=models.URLField(help_text='Enter the expire url that will work when campaign ends (must include http:// or https://)', max_length=300, verbose_name='Expire URL *'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='landing_url',
            field=models.URLField(help_text='Enter the landing url (must include http:// or https://)', max_length=300, verbose_name='Landing URL *'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='start_date',
            field=models.DateField(help_text="Enter the campaign's start date (format: YYYY-MM-DD)", verbose_name='Start Date *'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('suspended', 'Suspended'), ('declined', 'Declined')], help_text='Choose the campaing status', max_length=22, verbose_name='Status *'),
        ),
    ]
