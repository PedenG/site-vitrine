from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Prenom', max_length=100)
    lastName = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telephone', max_length=15)
    subject = forms.CharField(label='Sujet')
    message = forms.CharField(widget=forms.Textarea, label='Votre message')


