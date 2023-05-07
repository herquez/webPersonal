from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('admin/', admin.site.urls),
]
