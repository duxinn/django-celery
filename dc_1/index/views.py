from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    return HttpResponse('welcome')
