from django.shortcuts import redirect, render
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
def filter_leaderboard(request, id):
    categories = dict(CATEGORIES_NUM)
    data = Book.objects.filter(category=categories.get(id))

    context = {
        'products': data,
    }

    return render(request, "leaderboard.html", context)

@login_required(login_url='/login/')
def rate_button(request, item_id):
    if request.method == 'POST':
       book = Book.objects.get(pk=item_id) #Mengakses item yang ingin dimodifikasi
       book.rate += 1
       return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()

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
def get_item_json(request):
    book = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book))