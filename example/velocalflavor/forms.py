# example of definiton for all possible fields from
# Venezuelan localflavor

from django import newforms as forms
from django.contrib.localflavor.ve.forms import *

class VELocalForm(forms.Form):
    ve_dni_format = VEDNIField()
    ve_rif_format = VERIFField()
    ve_zip_code = VEZipCodeField()
    ve_phone_format = VEPhoneField()
    ve_regions = forms.CharField(label=_(u"Regions"), widget=VERegionsSelect())
    ve_states = forms.CharField(label=_(u"States"), widget=VEStateSelect())
