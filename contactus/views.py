from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import ContactUsInfo
from .forms import ContactUsForm

# Create your views here.
def contact_us_form_view(request):
    form = ContactUsForm(request.POST or None)
    successMsg = ""
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
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
