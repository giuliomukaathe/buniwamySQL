from django.contrib import admin
from contact.models import  CustomerMessage

# Register your models here
class CustomerMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message', 'date', )

admin.site.register(CustomerMessage, CustomerMessageAdmin)
# Register your models here.
