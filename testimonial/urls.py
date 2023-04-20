from testimonial import views
from django.urls import path

urlpatterns = [path("testimonial", views.Testi, name="Testi")]