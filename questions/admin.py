from django.contrib import admin

from .models import Date, Question, Quiz

admin.site.register(Question)
admin.site.register(Date)
admin.site.register(Quiz)
