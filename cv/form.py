from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nom', 'class': 'form-control'}))
    email = forms.EmailField( required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.NumberInput(attrs={'placeholder': 'Téléphone', 'class': 'form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Sujet', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Ecrivez votre message ici...', 'class': 'form-control', 'rows': '9'}), required=True)


