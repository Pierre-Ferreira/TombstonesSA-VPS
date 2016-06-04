from django import forms

from .models import FeedBack

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = [
            "fullname",
            "contactNo",
            "emailAddr",
            "type",
            "message",
        ]
        labels = {
            "fullname": ("Your name and surname"),
            "emailAddr": ("Your email address"),
            "contactNo": ("Your contact/cell number"),
            "type": ("What type is your feedback?"),
            "message": ("Your feedback"),
        }
