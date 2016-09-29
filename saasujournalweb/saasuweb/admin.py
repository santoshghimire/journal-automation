from django.contrib import admin

# Register your models here.
from .models import CSVInput, JournalEntry

admin.site.register(CSVInput)
admin.site.register(JournalEntry)
