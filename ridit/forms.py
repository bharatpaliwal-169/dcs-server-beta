from django import forms
from .models import School
from .models import Partner
from .models import Service
from django.contrib.admin import widgets  
from .models import Chauffer
from .models import Puc,Insurance,Rto

class DriveForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ('name','mobile','email','vehicle','gender','date','days','city')
        labels = {
            'name':'Full Name',
            'email':'Email Id',
            'mobile':'Mobile No',
            'vehicle' : 'Which vehicle you want to learn?',
            'date' : 'Date',
            'days' : 'Duration',
            'city' : 'City'
        }
        widgets = {'date':widgets.AdminDateWidget(attrs={'placeholder':'YYYY-MM-DD'}),
        }

    def __init__(self, *args, **kwargs):
        super(DriveForm,self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = "Select"
        self.fields['city'].empty_label = "Select"
        self.fields['vehicle'].empty_label = "Select"

class PartnerForm(forms.ModelForm):
    #service = forms.ModelMultipleChoiceField(queryset=Service.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Partner
        fields = ('name','contact','service','city','query')
        labels ={ 'name':'Full Name',
                  'contact':'Mobile No',
                  'service' : 'Which services you can provide',
                  'city':'Enter the cities in which you provide your services',
                  'query' : 'Enter your query'
                  }
        widgets = {'query': forms.Textarea(attrs={'placeholder': 'If you provide any additional service then please mention here'})
               }

    def __init__(self, *args, **kwargs):
        super(PartnerForm,self).__init__(*args,**kwargs)
        self.fields['service'].empty_label="Select"
        self.fields['city'].empty_label = "Select"
        self.fields['query'].required = False


class ChaufferForm(forms.ModelForm):

    class Meta:
        model = Chauffer
        fields = ('name','contact','email','address','date','pincode','days')
        labels = {
            'name':'Full Name',
            'email':'Email Id',
            'contact':'Mobile No',
            'address' : 'Address',
            'date' : 'Starting Date',
            'days' : 'Enter no of days (1-30)',
            'pincode' : 'Pincode'
        }
        widgets = {'date':widgets.AdminDateWidget(attrs={'placeholder':'YYYY-MM-DD'})}

class PucForm(forms.ModelForm):

    class Meta:
        model = Puc
        fields = ('name','contact','vehicle_no','exp_date','city','vehicle_type')
        labels = {
            'name':'Full Name',
            'contact':'Mobile No',
            'vehicle_no' : 'Vehicle No',
            'vehicle_type':'Vehicle Type',
            'exp_date' : 'Expiry Date',
            'city' : 'City'
        }
        widgets = {'exp_date':widgets.AdminDateWidget(attrs={'placeholder':'YYYY-MM-DD'})}

    def __init__(self, *args, **kwargs):
        super(PucForm,self).__init__(*args, **kwargs)
        self.fields['city'].empty_label = "Select"


class InsuranceForm(forms.ModelForm):

    class Meta:
        model = Insurance
        fields = ('name','contact','city','exp_date','ins_type')
        labels = {
            'name':'Full Name',
            'contact':'Mobile No',
            'city' : 'City',
            'exp_date' : 'Previous Insurance Expiry Date',
            'ins_type' : 'Type of Insurance',
        }
        widgets = {'exp_date':widgets.AdminDateWidget(attrs={'placeholder':'YYYY-MM-DD'})}

    def __init__(self, *args, **kwargs):
        super(InsuranceForm,self).__init__(*args, **kwargs)
        self.fields['city'].empty_label = "Select"
        self.fields['ins_type'].empty_label = "Select"

class RtoForm(forms.ModelForm):

    class Meta:
        model = Rto
        fields = ('name','contact','city','serv','others')
        labels = {
            'name':'Full Name',
            'contact':'Mobile No',
            'city' : 'City',
            'serv' : 'Services',
            'others' : 'Write your queries here',
        }
        widgets = {'others': forms.Textarea(attrs={'placeholder': 'If you want to specify any other service, then please mention here'})}

    def __init__(self, *args, **kwargs):
        super(RtoForm,self).__init__(*args, **kwargs)
        self.fields['city'].empty_label = "Select"
        self.fields['serv'].empty_label = "Select"
        self.fields['others'].required = False