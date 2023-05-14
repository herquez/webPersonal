from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from portfolio import urls as portfolio_urls

urlpatterns = [
    path('', core_views.home, name='home'),
    path('about/', core_views.about, name='about'),
    path('contact/', core_views.contact, name='contact'),
    path('portfolio/', include(portfolio_urls)),
    path('admin/', admin.site.urls),
]

from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)