from django.shortcuts import render, HttpResponse

template = """
<h1>Web Personal | Miguel Hernández</h1>

<ul>
    <li><a href='/'>Pagina de inicio</a></li>
    <li><a href='/about/'>Acerca de mi</a></li>
    <li><a href='/portfolio/'>Portafolio</a></li>
    <li><a href='/contact/'>Contacto</a></li>
</ul>
"""

def home(request):
    return HttpResponse(template + '<h2>Pagina de inicio</h2>')

def about(request):
    return HttpResponse(template + '<h2>Acerca de mi</h2>')

def portfolio(request):
    return HttpResponse(template + '<h2>Portafolio</h2>')

def contact(request):
    return HttpResponse(template + '<h2>Contacto</h2>')