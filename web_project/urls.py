
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from tracker import views as tracker_views
from django.conf import settings
from user_manager import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',tracker_views.home,name="home"),
    path('reports/',tracker_views.reports,name="reports"),
    path('patients/',tracker_views.patients,name="patients"),
    #path('tracker/',include('tracker.urls')),
    path('add_patient/',tracker_views.add_patient,name="add_patient"),
    path('signup/', user_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
