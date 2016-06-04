from django.contrib import admin

# Register your models here.

from contactus.models import ContactUsInfo

class ContactUsInfoModelAdmin(admin.ModelAdmin):
    list_display = ["fullname","emailAddr", "contactNo", "locationPersonal", "locationTombstone", "howManyTombstones", "installationDate"]
    list_display_links = ["fullname", "emailAddr"]
    list_filter = ["timeStamp", "locationTombstone"]
    search_fields = ["fullname", "locationTombstone"]
    class Meta:
        model= ContactUsInfo

admin.site.register(ContactUsInfo, ContactUsInfoModelAdmin)
