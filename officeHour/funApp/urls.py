from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('logReg/', views.logReg),
    path('login/', views.login),
    path('register/', views.register),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),
    path('notes/addNote/', views.addNote),
    path('notes/createNote/', views.createNote),
    path('notes/<int:id>/', views.viewNote),
    path('notes/<int:id>/edit/', views.editNote),
    path('notes/<int:id>/update', views.updateNote),
    path('notes/<int:id>/delete/', views.deleteNote),
    path('tasks/', views.tasks),
    path('tasks/addTask/', views.addTask),
    path('tasks/createTask/', views.createTask),
    path('tasks/<int:id>/', views.viewTask),
    path('tasks/<int:id>/edit/', views.editNote),
    path('tasks/<int:id>/update/', views.updateTask),
    path('tasks/<int:id>/delete/', views.deleteTask),
    path('uploads/', views.uploads),
    path('uploads/addUpload/', views.addUpload),
    path('uploads/createUpload/', views.createUpload),
    path('uploads/<int:id>/', views.viewUpload),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)