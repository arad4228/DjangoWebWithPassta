from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .forms import CommentForm
from .models import ForumPost, Category, Tag


class PostCreate(LoginRequiredMixin, CreateView):
    model = ForumPost
    fields = ['title', 'status', 'content', 'content_image', 'attached_file', 'category', 'tags']

    template_name = "forums/forumpost_form.html"

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/forums')

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PostCreate, self).get_context_data()
        context['Categories'] = Category.objects.all()
        context['No_Categoriy_Post_count'] = ForumPost.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = ForumPost
    fields = ['title', 'status', 'content', 'content_image', 'attached_file', 'category', 'tags']

    template_name = "forums/forumpost_form_update.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        context['Categories'] = Category.objects.all()
        context['No_Categoriy_Post_count'] = ForumPost.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context


class PostList(ListView):
    model = ForumPost        # 모델 객체 설정.
    ordering = '-pk'    # 정렬 방식 설정 = pk의 역순.

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['Categories'] = Category.objects.all()
        context['No_Categoriy_Post_count'] = ForumPost.objects.filter(category=None).count()
        return context


class PostDetail(DetailView):
    model = ForumPost

    def get_context_data(self, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['Categories'] = Category.objects.all()
        context['No_Categoriy_Post_count'] = ForumPost.objects.filter(category=None).count()
        context['comment_form'] = CommentForm
        return context


def show_category_posts(request, slug):
    if slug=='no-category' :  # 미분류 카테고리
        category = '미분류'
        forumpost_list = ForumPost.objects.filter(category=None)
    else :
        category = Category.objects.get(slug=slug)
        forumpost_list = ForumPost.objects.filter(category=category)

    context = {
        'Categories' :Category.objects.all(),
        'No_Categoriy_Post_count' : ForumPost.objects.filter(category=None).count(),
        'category' : category,
        'forumpost_list' : forumpost_list
    }
    return render(request, 'forums/forumpost_list.html', context)


def show_tag_posts(request, slug):
    tag = Tag.objects.get(slug=slug)
    forumpost_list = tag.post_set.all()

    context = {
        'Categories': Category.objects.all(),
        'No_Categoriy_Post_count': ForumPost.objects.filter(category=None).count(),
        'tag': tag,
        'forumpost_list': forumpost_list
    }
    return render(request, 'forums/forumpost_list.html', context)


def add_Comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(ForumPost, pk=pk)

        if request.method == 'POST':
            comment_Form = CommentForm(request.POST)
            if comment_Form.is_valid():
                # commit = false가 없으면 바로 DB에 저장된다.
                comment = comment_Form.save(commit=False)
                comment.post=post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied
    return None
