from django.contrib import admin
from django.urls import path
import summerApp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', summerApp.views.index, name="index"),
    path('create/', summerApp.views.create, name="create")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
