from django.contrib import admin
from letter.models import  Subscribers, MailMessage

# Register your models here
class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'country', 'region', 'email', 'date', )

class MailMessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'date', )

admin.site.register(Subscribers, SubscribersAdmin)
admin.site.register(MailMessage, MailMessageAdmin)
