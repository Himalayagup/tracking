from django import forms
from .models import Advertiser

# creating a form


class AdvertiserForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Advertiser

        # specify fields to be used
        fields = ["agency",
                  "company_name",
                  "first_name",
                  "last_name",
                  "email",
                  "advertiser_category",
                  "status",
                  ]
        # widgets = {'status': forms.RadioInput}
