from django.shortcuts import render, redirect

# Create your views here.
from forums.models import ForumPost, Category


def landing(request):
    return render(
        request,
        'main_page/landing.html',
        {
            'recent_posts': ForumPost.objects.order_by('-pk')[:3],
            'Categories': Category.objects.all(),
            'No_Categoriy_Post_count': ForumPost.objects.filter(category=None).count(),
        }
    )
