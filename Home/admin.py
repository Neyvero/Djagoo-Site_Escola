from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Category)


class AnswerAdmin(admin.StackedInline):
    model = Anwser


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Anwser)
