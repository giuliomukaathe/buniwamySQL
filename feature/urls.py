from django.urls import path
from feature import views


urlpatterns = [path("feature", views.feature, name="feature")]