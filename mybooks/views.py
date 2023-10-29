import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import UserProfile, User
from .models import Bookmark
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

CATEGORIES_NUM = [
    (1, "Literature & Fiction"),
    (2, "Mystery, Thriller & Suspense"),
    (3, "Religion & Spirituality"),
    (4, "Romance"),
    (5, "Science Fiction & Fantasy"),
]

@login_required(login_url='/login/')
def show_mybooks(request):
    user_profile = request.user
    bookmark = Bookmark.objects.filter(user=user_profile)
    context = {
        'bookmarked_books': bookmark,
        'categories' : CATEGORIES_NUM,
    }
    return render(request, 'mybooks.html', context)

def filter_category(request, id):
    categories = dict(CATEGORIES_NUM)
    user_profile = request.user
    bookmarked_books = Bookmark.objects.filter(user=user_profile)
    data = []

    for bookmark in bookmarked_books:
        if bookmark.book.category == categories.get(id):
            data.append(bookmark)

    context = {
        'products': data,
        'categories': CATEGORIES_NUM,
    }

    return render(request, "mybooks.html", context)

def get_bookmark_json(request):
    user_profile = request.user
    bookmarked_books = Bookmark.objects.filter(user=user_profile)
    category_filter = request.GET.get('category_filter')
    arr = []
    categories = dict(CATEGORIES_NUM)
    for bookmark in bookmarked_books:
        if bookmark.book.category == categories.get(int(category_filter)):
            obj_bookmark = {
                "pk": bookmark.pk,
                "user": bookmark.user.pk,
                "book": {
                    "title": bookmark.book.title,
                    "author": bookmark.book.author,
                    "category": bookmark.book.category,
                    "image_url": bookmark.book.image_url,
                    "rate": bookmark.book.rate,
                },
                "review": bookmark.review,
            }
            arr.append(obj_bookmark)
        elif int(category_filter) == 0:
            obj_bookmark = {
            "pk": bookmark.pk,
            "user": bookmark.user.pk,
            "book": {
                "title": bookmark.book.title,
                "author": bookmark.book.author,
                "category": bookmark.book.category,
                "image_url": bookmark.book.image_url,
                "rate": bookmark.book.rate,
            },
            "review": bookmark.review,
            }
            arr.append(obj_bookmark)

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
        bookmark = Bookmark.objects.get(pk=id)
        bookmark.review = review
        bookmark.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()




