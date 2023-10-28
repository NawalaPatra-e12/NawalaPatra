from django.shortcuts import redirect, render,get_object_or_404
from library.models import Book
from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.core import serializers
from main.models import User, UserProfile
from django.contrib.auth.decorators import login_required

CATEGORIES_NUM = [
    (1, "Literature & Fiction"),
    (2, "Mystery, Thriller & Suspense"),
    (3, "Religion & Spirituality"),
    (4, "Romance"),
    (5, "Science Fiction & Fantasy"),
]

def show_leaderboard(request):
    data = Book.objects.order_by('-rate')[:10]
    
    context = {
        'products': data,
        'categories': CATEGORIES_NUM,
    }

    return render(request, "leaderboard.html", context)

def filter_leaderboard(request, id):
    categories = dict(CATEGORIES_NUM)
    data = Book.objects.filter(category=categories.get(id)).order_by('-rate')[:10]

    context = {
        'products': data,
        'categories': CATEGORIES_NUM,
    }

    return render(request, "leaderboard.html", context)

@login_required(login_url='/login/')
def rate_button(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        book.rate += 1
        book.save()
     # Store the current URL in the session
        request.session['last_seen_page'] = request.META.get('HTTP_REFERER', '/')

    # Redirect back to the last seen page
    return HttpResponseRedirect(request.session.get('last_seen_page', '/'))
#