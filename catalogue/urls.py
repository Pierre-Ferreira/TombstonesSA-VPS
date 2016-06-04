from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

# from . import views
from .views import catalogue_view

urlpatterns = [
    url(r'^$', catalogue_view),
]
