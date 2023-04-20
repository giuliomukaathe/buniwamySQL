from django.urls import path
from letter import views


urlpatterns = [path("baseletter", views.baseletter, name="baseletter")]
