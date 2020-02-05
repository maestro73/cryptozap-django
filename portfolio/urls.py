from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import liqmonitor.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('ftx/', liqmonitor.views.ftx, name='ftx'),
    path('bitmex/', liqmonitor.views.bitmex, name='bitmex'),
    path('hitbtc/', liqmonitor.views.hitbtc, name='hitbtc')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
