from django import forms

class AdmissionForm(forms.Form):
    name = forms.CharField(max_length=10, label='Name')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=10, label='Phone')
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), label='Date of Birth')
    address = forms.CharField(widget=forms.Textarea, label='Address')

    