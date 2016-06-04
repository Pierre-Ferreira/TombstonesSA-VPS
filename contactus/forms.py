from django import forms

from .models import ContactUsInfo

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsInfo
        fields = [
            "fullname",
            "emailAddr",
            "contactNo",
            "locationPersonal",
            "locationTombstone",
            "howManyTombstones",
            "installationDate",
            "catalogueCodes",
            "colorTombstone",
            "otherInfo",
        ]
        labels = {
            "fullname": ("Your name and surname"),
            "emailAddr": ("Your email address"),
            "contactNo": ("Your contact/cell number"),
            "locationPersonal": ("Your location (City/Town)"),
            "locationTombstone": ("Location of tombstone installation (City/Town)"),
            "howManyTombstones": ("How many tombstones do you require?"),
            "installationDate": ("Date of installation"),
            "catalogueCodes": ("Any specific shape from the Catalogue that you like?<br> (Specify Codes)"),
            "colorTombstone": ("Color of tombstone"),
            "otherInfo": ("Any other information you would like to specify?"),
        }
