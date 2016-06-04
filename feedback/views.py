from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core import mail

from .models import FeedBack
from .forms import FeedBackForm

# Create your views here.

def feedback_form_view(request):
    form = FeedBackForm(request.POST or None)
    successMsg = ""
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        #message success
        # mail.send_mail('subject','message','pierre@tektite.biz',['pierre@tektite.biz'])
        messages.success(request, "Feedback has been submitted!")
        return HttpResponseRedirect('/feedback')
    # else:
    #     messages.error(request, "Error! Feedback not submitted.")

    # form = FeedBackForm()
    # if request.method == "POST":
    #     print request.POST.get("fullname")
    #     print request.POST.get("message")
    # instance = get_object_or_404(FeedBack, id=2)
    # queryset = FeedBack.objects.all()
    title = "Feedback"
    nbar = "feedback"
    context = {
        "form": form,
        "title": title,
        "nbar": nbar,
        # "object_list": queryset,
        # "pagename": "FEeDBACK"
    }
    return render(request, 'feedback_page.html', context)
    # return HttpResponse("<h1>CREATE</h1>")

# def feedback_read(request):
#     return HttpResponse("<h1>READ</h1>")
#
# def feedback_update(request):
#     return HttpResponse("<h1>UPDATE</h1>")
#
# def feedback_delete(request):
#     return HttpResponse("<h1>DELETE</h1>")
