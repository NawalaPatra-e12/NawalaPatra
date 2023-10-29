import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import UserProfile, User
from .models import Bookmark
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


@login_required(login_url='/login/')
def show_mybooks(request):
    user_profile = request.user
    bookmark = Bookmark.objects.filter(user=user_profile)
    return render(request, 'mybooks.html', {'bookmarked_books': bookmark})

CATEGORIES_NUM = [
    (1, "Literature & Fiction"),
    (2, "Mystery, Thriller & Suspense"),
    (3, "Religion & Spirituality"),
    (4, "Romance"),
    (5, "Science Fiction & Fantasy"),
]

def filter_category(request, id):
    categories = dict(CATEGORIES_NUM)
    user_profile = request.user
    bookmarked_books = Bookmark.objects.filter(user=user_profile)
    data = []

    for bookmark in bookmarked_books:
        if bookmark.book.category == categories.get(id):
            data.append(bookmark.book)

    context = {
        'products': data,
        'categories': CATEGORIES_NUM,
    }

    return render(request, "mybooks.html", context)

def get_bookmark_json(request):
    user_profile = request.user
    bookmarked_books = Bookmark.objects.filter(user=user_profile)
    arr = []
    for bookmark in bookmarked_books:
        obj_bookmark = {
            "pk":bookmark.pk, 
            "user":bookmark.user.pk, 
            "book": {
                "title": bookmark.book.title,  
                "author": bookmark.book.author,  
                "category": bookmark.book.category,  
                "image_url": bookmark.book.image_url,
                "rate": bookmark.book.rate,
            },
            "review":bookmark.review}
        arr.append(obj_bookmark)
    # return HttpResponse(serializers.serialize("json", arr), content_type="application/json")
    return JsonResponse({"result":arr})

def show_xml(request):
    user_profile = request.user
    data = Bookmark.objects.filter(user=user_profile)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    user_profile = request.user
    data = Bookmark.objects.filter(user=user_profile)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    user_profile = request.user
    data = Bookmark.objects.filter(user=user_profile)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    user_profile = request.user
    data = Bookmark.objects.filter(user=user_profile)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def remove_bookmark(request):
    if request.method == 'DELETE':
        raw_body_decoded = request.body.decode("utf-8")
        data = json.loads(raw_body_decoded)
        Bookmark.objects.get(pk=data["id"]).delete()

    return HttpResponse(b"OK", status = 200)

@csrf_exempt
def add_review_ajax(request, id):
    if request.method == 'POST':
        review = request.POST.get("review")
        print(review)
        bookmark = Bookmark.objects.get(pk=id)
        bookmark.review = review
        bookmark.save()
        print(bookmark.review)

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()


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


# @login_required(login_url='/login/')
# def show_mybooks(request):
#     return render(request, 'mybooks.html')

# def get_bookmark_json(request):
#     print(request)
#     if request.method == 'GET':
#         print("masuk")
#         user_profile = request.user.userprofile
#         bookmarked_books = user_profile.bookmarked_books.all()
#         book_data = [
#             {
#                 'title': book.title,
#                 'author': book.author,
#                 'category': book.category,
#                 'image_url': book.image_url,
#             }
#             for book in bookmarked_books
#         ]
#         print(book_data)
#         return JsonResponse({'bookmarked_books': book_data})

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


# @login_required(login_url='/login/')
# def show_mybooks(request):
#     user_profile = request.user.userprofile
#     bookmarked_books = user_profile.bookmarked_books.all()
#     return render(request, 'mybooks.html', {'bookmarked_books': bookmarked_books})




    # if request.method == 'GET':
    #     user_profile = request.user.userprofile
    #     bookmarked_books = user_profile.bookmarked_books.all()
    #     book_data = [
    #         {
    #             'title': book.title,
    #             'author': book.author,
    #             'category': book.category,
    #             'image_url': book.image_url,
    #         }
    #         for book in bookmarked_books
    #     ]
    #     return HttpResponse(serializers.serialize('json', bookmarked_books))

