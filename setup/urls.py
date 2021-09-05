from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('webs/', include('webs.urls')),
    path('accountant/', include('accountant.urls')),
    path('agent/', include('agent.urls')),
    path('manager/', include('manager.urls')),
    path('customer/', include('customer.urls')),
    path('', views.index, name='index'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
