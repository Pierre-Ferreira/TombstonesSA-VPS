from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import CatalogueImages

# Create your views here.
def catalogue_view(request):
    queryAllImages = CatalogueImages.objects.all()
    title = "Catalogue"
    nbar = "catalogue"
    context = {
        "title": title,
        "nbar": nbar,
        "queryAllImages": queryAllImages,
    }
    return render(request, 'catalogue_page.html', context)
