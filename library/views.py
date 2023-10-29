from django.shortcuts import get_object_or_404, redirect, render
from library.models import Book, Request
from django.db.models import Q
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from main.models import User, UserProfile
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


CATEGORIES_NUM = [
    (1, "Literature & Fiction"),
    (2, "Mystery, Thriller & Suspense"),
    (3, "Religion & Spirituality"),
    (4, "Romance"),
    (5, "Science Fiction & Fantasy"),
]

# Create your views here.
# Show main library page.
def show_library(request):
    data = Book.objects.all()
    
    context = {
        'products': data,
        'categories': CATEGORIES_NUM,
    }

    return render(request, "library.html", context)

# Function to search & filter books according to search term.
def search_products(request):
    if request.method == "POST":
        searched = request.POST['searched']
        words = searched.split()

        search_filter = Q()

        for word in words:
            search_filter &= Q(title__icontains=word) | Q(author__icontains=word) | Q(category__icontains=word)

        data = Book.objects.filter(search_filter)

        context={
            'searched': searched,
            'products': data,
            'categories': CATEGORIES_NUM,
        }

        return render(request, "library.html", context)
    
    else:
        return render(request, "library.html", {})

# Function to filter books according to category id.
def filter_category(request, id):
    categories = dict(CATEGORIES_NUM)
    data = Book.objects.filter(category=categories.get(id))

    context = {
        'products': data,
        'categories': CATEGORIES_NUM,
    }

    return render(request, "library.html", context)

@login_required(login_url='/login/')
def bookmark_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        user_profile = request.user.userprofile

        if book not in user_profile.bookmarked_books.all():
            user_profile.bookmarked_books.add(book)
    return redirect('library:show_library')  # Redirect back to the library page or another appropriate URL

# OTHER STUFF
def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_request_json(request):
    product_item = Request.objects.select_related("user")
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_request_ajax(request):
    if request.method == 'POST':

        user = request.user
        book_title = request.POST.get("book_title")
        book_author = request.POST.get("book_author")
        reason = request.POST.get("reason")

        new_product = Request(book_title=book_title, book_author=book_author, reason=reason, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
