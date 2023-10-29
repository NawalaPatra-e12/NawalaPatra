from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from mybooks.models import Bookmark


# Create your views here.
def show_main(request):
    if request.user.is_authenticated:
        user_profile = request.user
        bookmarked = Bookmark.objects.filter(user=user_profile)
        bookmarked_books = []
        counter = 0
        for bookmark in bookmarked:
            book = {
                    "title": bookmark.book.title,  
                    "author": bookmark.book.author,  
                    "category": bookmark.book.category,  
                    "image_url": bookmark.book.image_url,
                    "rate": bookmark.book.rate,
                    }
            bookmarked_books.append(book)
            counter += 1
            if counter == 5:
                break

        context = {
            'bookmarked' : bookmarked_books,
        }

        return render(request, "main.html", context)
    else:
        return render(request, "main.html")

def show_main(request):
    return render(request, "main.html")

# def show_library(request):
#     return render(request, show_library)
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

def get_username(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user_data = {
            'username': user.username,
        }
        return JsonResponse(user_data)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
