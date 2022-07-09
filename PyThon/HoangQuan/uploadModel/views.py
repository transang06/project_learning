from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm


# Create your views here.
def uploadFile(request):
    UF = UploadFileForm
    return render(request, 'uploadModel/fileUpload.html', {'UF': UF})


def getFile(request):
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse("Thanh cong")
