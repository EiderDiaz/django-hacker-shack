from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    # -> using HTTP response
    #return HttpResponse("si que si")
    # -> using loader
    #my_template = loader.get_template("index.html")
    #return render(my_template.render({},request))
    # -> using Render
    return render(request=request,
    template_name="index.html",
    context={})


def about(request):
    return render(request=request,
    template_name="about.html",
    context={})

def contact(request):
    return render(request=request,
    template_name="contact.html",
    context={})


