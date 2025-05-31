from django.shortcuts import render, redirect
from .models import Blog, Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm


def home(request):
    blogs = Blog.objects.all().order_by("-created_at")
    carousel = Blog.objects.all().order_by("-id")[:4]

    context = {"blogs": blogs, "carousel": carousel}
    return render(request, "blog/home.html", context)


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = blog.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect("blog_detail", pk=pk)
    else:
        form = CommentForm()

    context = {"blog": blog, "form": form, "comments": comments}
    return render(request, "blog/blog_detail.html", context)


def blog_like(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.likes += 1
    blog.save()
    return redirect("blog_detail", pk=pk)


def search(request):
    query = request.GET.get("q")
    if query:
        results = Blog.objects.filter(title__icontains=query)
    else:
        results = Blog.objects.all()

    context = {"results": results, "query": query}
    return render(request, "blog/search.html", context)
