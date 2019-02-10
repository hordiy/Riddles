from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Post, Category
from .forms import CategoryForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={0}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={0}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }
    return render(request, 'blog/index.html', context=context)

class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})

class PostCreate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})

    def post(self, request):
        bound_form = PostForm(request.POST)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'blog/post_create.html', context={'form': bound_form})

class PostUpdate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(instance=post)
        return render(request, 'blog/post_update.html', context={'form': bound_form, 'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'blog/post_update.html', context={'form': bound_form, 'post': post})

class PostDelete(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_delete.html', context={'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('posts_list_url'))

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories_list.html', context={'categories': categories})

class CategoryDetail(View):
    def get(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        return render(request, 'blog/category_detail.html', context={'category': category})

class CategoryCreate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request):
        form = CategoryForm()
        return render(request, 'blog/category_create.html', context={'form': form})

    def post(self, request):
        bound_form = CategoryForm(request.POST)

        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        return render(request, 'blog/category_create.html', context={'form': bound_form})

class CategoryUpdate(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        bound_form = CategoryForm(instance=category)
        return render(request, 'blog/category_update.html', context={'form': bound_form, 'category': category})

    def post(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        bound_form = CategoryForm(request.POST, instance=category)

        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        return render(request, 'blog/category_update.html', context={'form': bound_form, 'category': category})

class CategoryDelete(LoginRequiredMixin, View):
    raise_exception = True
    def get(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        return render(request, 'blog/category_delete.html', context={'category': category})

    def post(self, request, slug):
        category = Category.objects.get(slug__iexact=slug)
        category.delete()
        return redirect(reverse('categories_list_url'))
