from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from writersjam.models import Submission, Prompt
from django.core import serializers
from django.contrib.auth.decorators import login_required
import datetime
from library.models import Book
from main.models import User

# belom tau mau buat apa
GENRES_NUM = [
    (1, "Literature & Fiction"),
    (2, "Mystery, Thriller & Suspense"),
    (3, "Religion & Spirituality"),
    (4, "Romance"),
    (5, "Science Fiction & Fantasy"),
]

THEME_NUM = [
    (1, "Write a story about a small town librarian who discovers a secret message hidden in the margins of an old book."),
    (2, "A renowned detective receives an anonymous letter containing a series of cryptic clues during haloween."),
    (3, "About a mysterious ritual"),
    (4, "A secret relationship between a mafia boss and a daughter of a noble family"),
    (5, "Abnormal dimension gate appears out of nowhere are letting out mysterious monster and now normal humans have super power."),
]

def show_story(request):
    current_week = datetime.date.today().isocalendar()[1]

    # genre dan theme prompt sesuai week user access web
    prompt_num = current_week % 5
    if prompt_num == 0:
        prompt_num = 5
    theme = THEME_NUM[prompt_num - 1][1]
    genre = GENRES_NUM[prompt_num - 1][1]

    try:
        prompt = Prompt.objects.get(week=current_week)
    except Prompt.DoesNotExist:
        # If not, create a new one
        prompt = Prompt.objects.create(theme=theme, week=current_week, genre=genre)

    story_data = Submission.objects.filter(prompt=prompt) 

    book_rec = Book.objects.all()

    context = {
        'story' : story_data,
        'prompt' : prompt,
        'books' : book_rec,
    }
    return render(request, "writer.html", context)

def filter_genre(request):
    current_week = datetime.date.today().isocalendar()[1]

    # genre dan theme prompt sesuai week
    prompt_num = current_week % 5
    if prompt_num == 0:
        prompt_num = 5
    theme = THEME_NUM[prompt_num - 1][1]
    genre = GENRES_NUM[prompt_num - 1][1]

    prompt = Prompt.objects.get(week=current_week)
    book_genre = Book.objects.filter(category = genre)

    context = {
        'books' : book_genre,
        'prompt' : prompt,
    }
    return render(request, "writer.html", context)

# view json
def story_json(request):
    current_week = datetime.date.today().isocalendar()[1]
    prompt = Prompt.objects.get(week=current_week)
    story = Submission.objects.filter(prompt=prompt)
    return HttpResponse(serializers.serialize('json', story), content_type='application/json')

def story_json_id(request, id):
    story = Submission.objects.get(pk=id)
    return HttpResponse(serializers.serialize('json', [story]), content_type='application/json')

# view xml
def story_xml(request):
    current_week = datetime.date.today().isocalendar()[1]
    prompt = Prompt.objects.get(week=current_week)
    story = Submission.objects.filter(prompt=prompt)
    return HttpResponse(serializers.serialize('xml', story), content_type='application/xml')

def story_xml_id(request, id):
    story = Submission.objects.get(pk=id)
    return HttpResponse(serializers.serialize('xml', [story]), content_type='application/xml')

def delete_story(request, id):
    Submission.objects.get(pk=id).delete()
    return HttpResponseRedirect(reverse('writersjam:show_story'))

def get_story_json(request):
    current_week = datetime.date.today().isocalendar()[1]
    prompt = Prompt.objects.get(week=current_week)
    story = Submission.objects.filter(prompt=prompt)
    return HttpResponse(serializers.serialize('json', story))

@login_required(login_url='/login/')
@csrf_exempt
def submit_story_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        story = request.POST.get("story")
        # anonymous = request.POST.get("anonymous") == 'true'
        date = datetime.datetime.now()

        # buat username
        user = request.user
        username = request.user.username
        # username = 'Anonymous' if anonymous else request.user.username
        
        current_week = datetime.date.today().isocalendar()[1]
        prompt = Prompt.objects.get(week=current_week)

        new_story = Submission(title=title, story=story, date=date, prompt=prompt, user=user, username=username)
        new_story.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()