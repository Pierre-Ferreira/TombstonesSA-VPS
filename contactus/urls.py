from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

# from . import views
from views import contact_us_form_view

urlpatterns = [
    url(r'^$', contact_us_form_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
