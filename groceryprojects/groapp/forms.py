from django import forms

class ShippingForm(forms.Form):
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    

class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16)
    expiration_date = forms.DateField()



from django import forms
from django.forms import ModelForm
from .models import Wish


class WishForm(ModelForm):
    
    wishtitle = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    wish = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    link = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    is_achieved = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input mt-0'}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control'}))
    
    class Meta:
        
        
        model=Wish
        fields=('wishtitle','wish','link','is_achieved','image')


        labels={
            'wishtitle':'Wish Title',
            'wish':'Wish',
            'link':'Link',
            'is_achieved':'Is Achieved',
            'image':'Image'
        }



from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['status', 'profile', 'booking_id', 'quantity', 'book_date', 'total']
