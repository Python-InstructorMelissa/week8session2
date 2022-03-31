from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('logout/', views.logout),
    path('register/', views.register),
    path('login/', views.login),
    path('dashboard/', views.dashboard),
    # Images / Favorites
    path('images/add/', views.addImages),
    path('images/create/', views.createImage),
    path('images/upload/', views.createUpload),
    path('images/nasa/', views.nasaImage),
    path('images/looneyToons', views.looneyToons),
    # Weather / Forcast
    path('weather/', views.weather),
    path('weather/save/', views.saveWeather),
    # Users / Profile
    path('users/', views.users),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)