from django.urls import path, include
from restaurant.api.urls import urlpatterns as api_urlpatterns
from restaurant.views import MenuView

urlpatterns = [
    path("", MenuView.as_view(), name="menu"),

    path("api/", include(api_urlpatterns))
]