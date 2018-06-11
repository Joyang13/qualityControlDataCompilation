from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('inner/', views.upload, name='inner'),
    path('outter/', views.outter, name = 'outter'),
    path('media/inner_form/$', views.upload, name = 'inner_upload'),
    path('media/outter_form/$', views.outter, name = 'outter_upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)