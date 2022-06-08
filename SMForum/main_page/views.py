from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from forums.models import ForumPost, Category, User
from forums.forms import UpdateUserForm


def update_user(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/about_me/')
    else:
        form = UpdateUserForm(instance=request.user)
    context = {
        'Categories': Category.objects.all(),
        'No_Categoriy_Post_count': ForumPost.objects.filter(category=None).count(),
        'form': form,
    }
    return render(request, 'main_page/main_page_user_update.html', context)


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


def about_me(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user.username)
        return render(
            request, 'main_page/about_me.html',
            {
                'Categories': Category.objects.all(),
                'No_Categoriy_Post_count': ForumPost.objects.filter(category=None).count(),
                'User':user,
            }
        )
    else:
        raise PermissionDenied
