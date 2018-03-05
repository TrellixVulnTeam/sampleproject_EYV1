from django.contrib import admin
from polls.models import Choice
from polls.models import Question

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date')
    fieldsets = [
        ('Question text',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)