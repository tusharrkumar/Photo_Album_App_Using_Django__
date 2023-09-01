from django.urls import path
from photoes.views import *
urlpatterns = [
    path('',gallery,name='gallery'),
    path('photo/<str:pk>',viewPhoto,name='photo'),
    path('add/',addPhoto,name='add'),
    path('delete/<int:id>/',deletePhoto, name='deletePhoto'), 
]