import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import UserProfile, User
from library.models import Book
from .models import Bookmark
from django.core import serializers


# Create your views here.
# def show_mybooks(request):

#     return render(request, "mybooks.html")

# def show_mybooks(request):
#     # nge get user
#     # get bookmark dari user itu
#     user_profile = request.user.userprofile
#     # bookmark = Bookmark.objects.all()
#     bookmarked_books = user_profile.bookmarked_books.all()
#     context = {
#         'bookmarked_books' : bookmarked_books
#     }

#     # return HttpResponse(serializers.serialize('json', bookmark), content_type='application/json')
#     return render(request, 'mybooks.html', context)


@login_required(login_url='/login/')
def show_mybooks(request):
    return render(request, 'mybooks.html')

def get_bookmark_json(request):
    print(request)
    if request.method == 'GET':
        print("masuk")
        user_profile = request.user.userprofile
        bookmarked_books = user_profile.bookmarked_books.all()
        book_data = [
            {
                'title': book.title,
                'author': book.author,
                'category': book.category,
                'image_url': book.image_url,
            }
            for book in bookmarked_books
        ]
        print(book_data)
        return JsonResponse({'bookmarked_books': book_data})

# @login_required(login_url='/login/')
# def show_mybooks(request):
#     print(request)
#     if request == 'GET':
#         print("masuk")
#         user_profile = request.user.userprofile
#         bookmarked_books = user_profile.bookmarked_books.all()
#         book_data = [{'title': book.title, 'author': book.author, 'category': book.category} for book in bookmarked_books]
#         return HttpResponse(serializers.serialize('json', bookmarked_books))
#         # return JsonResponse({'bookmarked_books': book_data})

#     return render(request, 'mybooks.html')

# def get_bookmark_json(request):
#     user_profile = request.user.userprofile
#     bookmarked_books = user_profile.bookmarked_books.all()
#     return HttpResponse(serializers.serialize('json', bookmarked_books))

# def delete_bookmark_ajax(request):
#     if request.method == 'DELETE':
#         raw_body_decoded = request.body.decode("utf-8")
#         data = json.loads(raw_body_decoded)
#         user_profile = request.user.userprofile
#         bookmark_book = user_profile


#     return HttpResponse(b"OK", status = 200)