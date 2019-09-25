from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .form import ContactForm

def index(request):
    return render(request, 'cv/index.html')

def mainpage(request):
    return render(request, 'cv/mainpage.html')


def contact(request):
    return render(request, 'cv/contact.html')


def about(request):
    return render(request, 'cv/about.html')


def contact(request):
    titre = 'Contact'
    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message'] + ' Email : ' + form.cleaned_data['email'] + ' Téléphone : ' + form.cleaned_data['phone']

            send_mail(subject,message, 'server@glen-peden.fr', ['glenpedenn@gmail.com'])
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'cv/contact.html', {'form': form, 'titre': titre})


