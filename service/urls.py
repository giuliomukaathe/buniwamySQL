from django.urls import path
from service import views
urlpatterns = [path("service", views.service, name="service")]