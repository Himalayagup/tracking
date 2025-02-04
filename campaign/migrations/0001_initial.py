# Generated by Django 3.0.3 on 2021-02-02 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('advertiser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('campaign_name', models.CharField(help_text='Enter the campaign name', max_length=235, verbose_name='Campaign Name')),
                ('landing_url', models.URLField(help_text='Enter the landing url (must include http:// or https://)', max_length=300, verbose_name='Landing URL')),
                ('expire_url', models.URLField(help_text='Enter the expire url that will work when campaign ends (must include http:// or https://)', max_length=300, verbose_name='Expire URL')),
                ('start_date', models.DateField(help_text="Enter the campaign's start date (format: YYYY-MM-DD)", verbose_name='Start Date')),
                ('end_date', models.DateField(help_text="Enter the campaign's end date (format: YYYY-MM-DD)", verbose_name='End Date')),
                ('campaign_type', models.CharField(choices=[('cpl', 'Cost Per Lead'), ('cpc', 'Cost Per Click'), ('cpi', 'Cost Per Impression'), ('cpa', 'Cost Per Action'), ('cpv', 'Cost Per Visit'), ('cps', 'Cost Per Sale'), ('cpinstall', 'Cost Per Install'), ('cpo', 'Cost Per Open'), ('cpsm', 'Cost Per Sent Mailer(s)')], help_text='Select the campaing types', max_length=22, verbose_name='Campaign Type')),
                ('campaign_category', models.CharField(blank=True, choices=[('banking', 'Banking'), ('matrimony', 'Matrimony'), ('job', 'Job'), ('education', 'Education'), ('finance', 'Finance'), ('insurance', 'Insurance'), ('securities', 'Securities'), ('automobile', 'Automobile'), ('travel_holidays', 'Travel and Holidays'), ('realestate', 'Real Estate'), ('ecommerce', 'E Commerce'), ('classified', 'Classified'), ('recharge_ecommerce', 'Recharge & E Commerce'), ('recharge', 'Recharge'), ('jewellery', 'Jewellery')], help_text='Select the campaing category', max_length=22, null=True, verbose_name='Campaign Category')),
                ('comment', models.TextField(blank=True, help_text='Any Comment(s)?', null=True, verbose_name='Comments')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('suspended', 'Suspended'), ('declined', 'Declined')], help_text='Choose the advertiser status', max_length=22, verbose_name='Status')),
                ('campaign_key', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('advertiser', models.ForeignKey(blank=True, help_text='Advertiser Company Name', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertiser_company', to='advertiser.Advertiser')),
            ],
        ),
        migrations.CreateModel(
            name='CampaignToPublisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active')], default='pending', help_text='Choose the publisher status', max_length=22, verbose_name='Status')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaign.Campaign')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Publisher')),
            ],
            options={
                'unique_together': {('user', 'campaign')},
            },
        ),
        migrations.AddField(
            model_name='campaign',
            name='publisher_campaign',
            field=models.ManyToManyField(through='campaign.CampaignToPublisher', to='accounts.Publisher'),
        ),
    ]
