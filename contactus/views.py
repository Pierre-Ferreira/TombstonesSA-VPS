from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.core.mail import send_mail

from .models import ContactUsInfo
from .forms import ContactUsForm

# Create your views here.
def contact_us_form_view(request):
    form = ContactUsForm(request.POST or None)
    successMsg = ""
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #send email to pierre@tekite.biz with details.
        custFullName = form.cleaned_data['fullname']
        custEmailAddr = form.cleaned_data['emailAddr']
        custContactNo = form.cleaned_data['contactNo']
        custLocationPersonal = form.cleaned_data['locationPersonal']
        custLocationTombstone = form.cleaned_data['locationTombstone']
        custHowManyTombstones = form.cleaned_data['howManyTombstones']
        custInstallationDate = form.cleaned_data['installationDate']
        custCatalogueCodes = form.cleaned_data['catalogueCodes']
        custColorTombstone = form.cleaned_data['colorTombstone']
        custOtherInfo = form.cleaned_data['otherInfo']
        alertEmailSubj = 'Tombstone/Memorial form submission received'
        alertEmailMessage = "\nfullname: %s" % custFullName
        alertEmailMessage += "\nemailAddr: %s" % custEmailAddr
        alertEmailMessage += "\ncontactNo: %s" % custContactNo
        alertEmailMessage += "\nlocationPersonal: %s" % custLocationPersonal
        alertEmailMessage += "\nlocationTombstone: %s" % custLocationTombstone
        alertEmailMessage += "\nhowManyTombstones: %s" % custHowManyTombstones
        alertEmailMessage += "\ninstallationDate: %s" % custInstallationDate
        alertEmailMessage += "\ncatalogueCodes: %s" % custCatalogueCodes
        alertEmailMessage += "\ncolorTombstone: %s" % custColorTombstone
        alertEmailMessage += "\notherInfo: %s" % custOtherInfo
        send_mail(alertEmailSubj, alertEmailMessage, settings.EMAIL_HOST_USER,['pierre@tektite.biz'], fail_silently=False)
        #send email to form submitter to confirm that info has been received.
        custEmailSubj = 'Tombstone/Memorial form submission received'
        custEmailMesssage = 'Thank you,\nyour info have been received. Someone will contact with you soon.'
        custEmailMesssage += "\n\nWarm regards,\n sales@tombstones-memorials-sa.co.za"
        custEmailMesssage += "\n www.tombstones-memorials-sa.co.za"
        send_mail(custEmailSubj, custEmailMesssage, settings.EMAIL_HOST_USER,[custEmailAddr], fail_silently=False)
        #message success
        messages.success(request, "Your request has been submitted!")
        return HttpResponseRedirect('/contactus')
    title = "Contact Us"
    nbar = "contactus"
    context = {
        "form": form,
        "title": title,
        "nbar": nbar,
    }
    return render(request, 'contact_us_page.html', context)
