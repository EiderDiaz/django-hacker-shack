from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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


# the order of the inheritance of classes mathers
# if i switch LoginRequiredMixin, TemplateView to :  TemplateView, LoginRequiredMixin the auth features of LoginRequiredMixin are lost
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"


