from django import forms
from django.forms import ModelForm
from .models import *

class GroupTourForm(ModelForm):
    class Meta:
        model = GroupTour
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['sold_out']:
                self.fields[field].widget.attrs['class'] = 'form-control'

class ItineraryForm(ModelForm):
    class Meta:
        models = Itinerary
        exclude = ['group_tour']

class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = '__all__'

class AddOnForm(ModelForm):
    class Meta:
        model = AddOn
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('package', 'add_on', 'consent')

    package = forms.ModelChoiceField(
        queryset=Package.objects.none(),
        widget=forms.Select(attrs={'id': 'package-id'}),
        required=True,
        empty_label=None,
    )

    add_on = forms.ModelChoiceField(
        queryset=AddOn.objects.none(),
        widget=forms.Select(attrs={'id': 'add-on-id'}),
    )

    def __init__(self, *args, **kwargs):
        packages = kwargs.pop('packages', None)
        add_ons = kwargs.pop('add_ons', None)
        super().__init__(*args, **kwargs)

        if packages is not None:
            self.fields['package'].id = 'package-id'
            self.fields['package'].queryset = packages
        if add_ons is not None:
            self.fields['add_on'].id = 'add-on-id'
            self.fields['add_on'].queryset = add_ons

        self.fields['consent'].label = 'I Agree to the Terms & Conditions'

        for field in self.fields:
            if field not in ['package', 'add_on', 'consent']:
                self.fields[field].widget.attrs['class'] = 'form-control'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
