from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', views.job_list, name='job_list'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

