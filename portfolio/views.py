from django.shortcuts import render
from .models import Project

def portfolio(request):
    projects = Project.objects.filter(deleted__isnull=True)
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio.html', context)
