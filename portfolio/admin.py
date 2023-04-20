from django.contrib import admin
from portfolio.models import  Portfolio

# Register your models here
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('service', 'link','date', )

admin.site.register(Portfolio, PortfolioAdmin)
