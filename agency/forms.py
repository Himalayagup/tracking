from django import forms
from .models import Agency

# creating a form


class AgencyForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Agency

        # specify fields to be used
        fields = [
            "agency_name",
            "agency_address",
            "contact_person",
            "email",
            "contact_number",
            "alternate_number",
        ]
