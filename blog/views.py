from django.shortcuts import render
from .models import Blog, Comment
from django.shortcuts import get_object_or_404


def home(request):
    blogs = Blog.objects.all().order_by("-created_at")
    carousel = Blog.objects.all().order_by("-id")[:4]

    context = {"blogs": blogs, "carousel": carousel}
    return render(request, "blog/home.html", context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/blog_detail.html", {"blog": blog})
