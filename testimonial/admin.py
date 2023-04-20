from django.contrib import admin
from testimonial.models import  Testimonial

# Register your models here
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'proffession', 'message', )

admin.site.register(Testimonial, TestimonialAdmin)