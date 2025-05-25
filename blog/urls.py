from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("blog/<str:pk>/", views.blog_detail, name="blog_detail"),
]
