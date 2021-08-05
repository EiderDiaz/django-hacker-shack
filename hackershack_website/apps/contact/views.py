from django import forms
from django.shortcuts import render
from .forms import ContactForm

def contact(request):
    if request.method  == "GET" :
        form = ContactForm()
        return render(request=request,
        template_name="contact.html",
        context={"form":form})
    else :
        raise NotImplementedError