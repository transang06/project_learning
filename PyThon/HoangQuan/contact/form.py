from django import forms


# class contact_Form(forms.ModelForm):
#     class Meta:
#         model = ContactForm
#         fields = ['username', 'email', 'body']
class contact_Form(forms.Form):
    username = forms.CharField(max_length=250)
    email = forms.EmailField()
    body = forms.CharField(widget= forms.Textarea)
