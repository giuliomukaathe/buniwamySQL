from django.contrib import admin
from .models import CustomerMessageQuote

class CustomerMessageQuoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'service', 'message', 'date', )

# Register your models here.
admin.site.register(CustomerMessageQuote, CustomerMessageQuoteAdmin)