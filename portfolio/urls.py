from django.urls import path
from portfolio import views

urlpatterns = [
    path('port/', views.portfolio, name='portfolio'),
]