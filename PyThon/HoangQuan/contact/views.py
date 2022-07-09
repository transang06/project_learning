from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from contact.form import contact_Form
from contact.models import ContactForm


# Create your views here.
# def contact(request):
#     context = {'cf': contact_Form}
#     return render(request, 'contact/contact.html', context)
# def getContact(request):
#     if request.method == "POST":
#         cf = contact_Form(request.POST)
#         if cf.is_valid():
#             cf.save()
#             return HttpResponse("sava success")

class contact(View):

    def get(self, request):
        context = {'cf': contact_Form}
        return render(request, 'contact/contact.html', context)

    def post(self, request):
        if request.method == "POST":
            cf = contact_Form(request.POST)
            if cf.is_valid():
                saveCF = ContactForm(username=cf.cleaned_data['username'],
                                     email=cf.cleaned_data['username'],
                                     body=cf.cleaned_data['username'])
                saveCF.save()
                return HttpResponse("sava success")
        else:
            return HttpResponse("not post")
