from django.shortcuts import render

# Create your views here.
def show_main(request):
    return render(request, "main.html")

def show_library(request):
    return render(request, show_library)
