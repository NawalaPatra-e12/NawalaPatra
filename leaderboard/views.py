from django.shortcuts import render
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound

def show_leaderboard(request):
    data = Book.objects.all()
    
    context = {
        'products': data,
    }
    return render(request, "leaderboard.html", context)

@csrf_exempt
def rate_button(request, item_id):
    if request.method == 'POST':
        book = Book.objects.get(pk=item_id) #Mengakses item yang ingin dimodifikasi
        book.user = request.user
        if book.amount > 0:
            book.amount += 1
            book.save()
        return HttpResponse(b"ADDED", status=201)
    return HttpResponseNotFound()