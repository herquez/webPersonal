from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("<h1>Home page</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")