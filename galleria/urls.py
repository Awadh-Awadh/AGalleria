from . import views
from django.urls import path

'''
All url patterns that creates all routes in the gallery apps
Include dynamic routing using the pk of each image
'''

urlpatterns = [
  path('', views.index, name = 'index'),
  path('upload/', views.upload, name = 'upload'),
  path('details/<int:pk>', views.details, name = 'details'),
  path('search/',views.search, name = 'search')
]