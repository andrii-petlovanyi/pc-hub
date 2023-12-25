from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import price_chart

urlpatterns = [
    path('price_chart', price_chart, name='price_chart')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
