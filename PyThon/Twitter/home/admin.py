from django.contrib import admin

from .models import Question


# class ChoiceInline(admin.StackedInline):


admin.site.register(Question)
# admin.site.register(Choice)
