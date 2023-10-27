from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import UserProfile, User
from library.models import Book


# Create your views here.
@login_required(login_url='/login/')
# def show_mybooks(request):

#     return render(request, "mybooks.html")

def show_mybooks(request):
    user_profile = request.user.userprofile
    bookmarked_books = user_profile.bookmarked_books.all()
    return render(request, 'mybooks.html', {'bookmarked_books': bookmarked_books})