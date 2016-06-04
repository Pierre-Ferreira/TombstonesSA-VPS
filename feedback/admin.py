from django.contrib import admin

# Register your models here.

from feedback.models import FeedBack

class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ["fullname","emailAddr", "contactNo", "type", "timeStamp"]
    list_display_links = ["fullname", "type"]
    list_filter = ["timeStamp", "type"]
    search_fields = ["fullname", "message"]
    class Meta:
        model= FeedBack

admin.site.register(FeedBack, FeedbackModelAdmin)
