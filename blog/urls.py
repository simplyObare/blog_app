from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("blog/<str:pk>/", views.blog_detail, name="blog_detail"),
    path("blog/<str:pk>/like/", views.blog_like, name="blog_like"),
    path("search/", views.search, name="search"),
]
