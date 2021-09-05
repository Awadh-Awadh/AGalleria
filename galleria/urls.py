from . import views
from django.urls import path


urlpatterns = [
  path('', views.index, name = 'index'),
  path('upload/', views.upload, name = 'upload')
]