from django import forms

from uploadModel.models import UpForm


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UpForm
        fields = ['title', 'image', 'body']