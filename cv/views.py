from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def home_page(request):
    pass

# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})