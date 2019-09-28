from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .form import ContactForm


def index(request):
    return render(request, 'cv/index.html')


def mainpage(request):
    return render(request, 'cv/mainpage.html')


def contact(request):
    return render(request, 'cv/contact.html')


def about(request):
    return render(request, 'cv/about.html')


def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message'] + 'Nom : ' + form.cleaned_data['name'] + 'Email : ' + email +' Téléphone : ' + form.cleaned_data['phone']
            try:
                send_mail(subject,message, email, ['glenpedenn@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()

    return render(request, 'cv/contact.html', {'form': form})


