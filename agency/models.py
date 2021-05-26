from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.


class Agency(models.Model):
    agency_name = models.CharField("Agency Name *",
                                   help_text="Enter the agency name",
                                   max_length=200,)
    agency_address = models.CharField("Agency's Address/City *",
                                      help_text="Enter the agency's address/city",
                                      max_length=300,)
    contact_person = models.CharField("Contact Person's Name *",
                                      help_text="Enter the agency's contact person's name",
                                      max_length=150,)
    email = models.EmailField("Agency/Contact Person's Mail ID *",
                              help_text="Enter the agency/contact person's mail id",
                              max_length=400,)
    contact_number = models.BigIntegerField("Agency's Contact Number *",
                                            help_text="Enter the agency's contact number",
                                            validators=[MaxValueValidator(9999999999)],)
    alternate_number = models.BigIntegerField("Alternate Contact Number",
                                              help_text="Enter the agency's alternate number",
                                              null=True, blank=True,
                                              validators=[MaxValueValidator(9999999999)],)

    def __str__(self):
        return self.agency_name

    def get_absolute_url(self):
        return reverse('agencylist')
