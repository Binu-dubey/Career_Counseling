from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'category', 'subcategory']
    search_fields = ['question_text']
    list_editable = ('category', 'subcategory')  # Allows you to edit these fields directly from the list view
    list_filter = ['category', 'subcategory']

admin.site.register(Question, QuestionAdmin)

