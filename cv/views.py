from django.shortcuts import render
from django import forms


def mainpage(request):
    titre = 'Bienvenue sur mon site'
    return render(request, 'cv/accueil.html', {'titre': titre})


def contact(request):
    titre = 'Contact'
    return render(request, 'cv/contact.html', {'titre': titre})


def cv(request):
    titre = 'CV'
    return render(request, 'cv/cv.html', {'titre': titre})


def blog(request):
    titre = 'Blog'
    return render(request, 'cv/blog.html', {'titre': titre})


class Form(forms.Form):
    name = forms.CharField(label='Prenom', max_length=100)
    lastName = forms.CharField(label='Nom', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.Textarea(label='Votre Message')


