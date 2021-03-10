from other_pages.models import GeneralSettings
from django.core import paginator
from social_media.models import SocialMedia
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, PostCategory
from .forms import postCreateForm
from django.db.models import F, Q
from urllib.parse import quote_plus


def global_data(request):
    return {
        'general_setting': GeneralSettings.objects.first(),
        'categories': PostCategory.objects.all(),
        'social_media': SocialMedia.objects.filter(status=1),
        'posts': Post.objects.all().order_by('-created_at')
    }


# Create your views here.
def homepage(request):
    posts = Post.objects.all().order_by('-created_at')
    categories = PostCategory.objects.all()
    feature_posts = Post.objects.filter(feature=True)
    popular_posts = Post.objects.all().order_by('-view_quantity')[:3]

    # for pagination
    paginator = Paginator(posts, 6)  # 4 item each page
    page = request.GET.get('page')  # get page no
    posts = paginator.get_page(page)

    context = {
        "title": "Home Page",
        "posts": posts,
        "categories": categories,
        "feature_posts": feature_posts,
        "popular_posts": popular_posts,
    }
    return render(request, 'posts/index.html', context)


def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)

    # increment view_quantity value
    Post.objects.filter(slug=slug).update(view_quantity=F('view_quantity') + 1)

    # related post
    related_post = Post.objects.filter(category=post.category_id)[:4]

    context = {
        "title": "Post Details",
        "post": post,
        "related_posts": related_post,
        "share_string": quote_plus(post.title),
    }
    return render(request, 'posts/post_details.html', context)


def post_create(request):
    form = postCreateForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data['title'])
            print(form.cleaned_data['content'])
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect('posts:home')
    context = {
        "title": "Post Create",
        "form": form,
    }
    return render(request, 'posts/post_create.html', context)


def blog_search(request):
    query = request.GET.get('qry')
    if query is not None:
        object_list = Post.objects.filter(
            Q(title__contains=query) | Q(content__contains=query)
        )
    context = {
        "title": "Post search",
        "posts": object_list,
        "query_string": query,
    }
    return render(request, 'posts/post_search_result.html', context)


def category_wise_post(request, slug):
    post_category = PostCategory.objects.filter(slug=slug).first()
    post_by_cate = Post.objects.filter(category=post_category.id)

    context = {
        "title": "Post Details",
        "posts": post_by_cate,
        "category_name": post_category.title,
    }
    return render(request, 'posts/category_wise_post.html', context)
