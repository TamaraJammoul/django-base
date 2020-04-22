
from django.contrib import admin
from django.urls import path, include
from . import views
from . views import Au
from rest_framework import routers
from .views import Bookviewset
router = routers.DefaultRouter()
router.register('books', Bookviewset)
urlpatterns = [
    #path('', views.first),
    #path('au', Au.as_view()),
    #path('sec', views.sec),
    path('', include(router.urls))
]
