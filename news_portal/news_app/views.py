from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden
from .models import News
from .forms import NewsForm, CustomUserCreationForm, UserUpdateForm

def home_view(request):
    news_list = News.objects.all().order_by('-date_created')
    paginator = Paginator(news_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

def news_detail_view(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news': news})

@login_required
def news_create_view(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, 'Новость добавлена!')
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form, 'title': 'Добавить новость'})

@login_required
def news_edit_view(request, pk):
    news = get_object_or_404(News, pk=pk)
    if news.author != request.user:
        return HttpResponseForbidden("Вы не можете редактировать чужую новость.")
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новость обновлена.')
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'news_form.html', {'form': form, 'title': 'Редактировать новость'})

@login_required
def news_delete_view(request, pk):
    news = get_object_or_404(News, pk=pk)
    if news.author != request.user:
        return HttpResponseForbidden("Вы не можете удалить чужую новость.")
    if request.method == 'POST':
        news.delete()
        messages.success(request, 'Новость удалена.')
        return redirect('home')
    return render(request, 'news_confirm_delete.html', {'news': news})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.first_name}!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль обновлён.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})

@login_required
def profile_delete_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Аккаунт удалён.')
        return redirect('home')
    return render(request, 'profile_confirm_delete.html')