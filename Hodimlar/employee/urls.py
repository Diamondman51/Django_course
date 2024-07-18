from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('hodimlar/<int:pk>/', hodim, name='hodim')
]