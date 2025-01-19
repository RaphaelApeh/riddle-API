from django.urls import path

from . import views

urlpatterns = [
    path("", views.home_page_view, name="home-view"),
    path('riddle/', views.riddle_view, name="riddle-view")
]