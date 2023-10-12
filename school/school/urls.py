#Import file for Media derectory Set
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path, include
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    # For Another Apps
    path('student/', include('student.urls')),
    path('teacher/', include('teacher.urls')),
]


#For Media Setup
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
