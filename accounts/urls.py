# This whole file is now antiquated by allauth apps functionality
from django.urls import path

from .views import SignupPageView


urlpatterns = [
    path("signup/", SignupPageView.as_view(), name="signup"),
]
