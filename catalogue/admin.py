from django.contrib import admin

# Register your models here.
from catalogue.models import CatalogueImages

class CatalogueImagesAdmin(admin.ModelAdmin):
    list_display = ['title', "desc", 'image']
    list_display_links = ["title", "desc"]
    search_fields = ["title", "desc"]
    class Meta:
        model= CatalogueImages

admin.site.register(CatalogueImages, CatalogueImagesAdmin)
