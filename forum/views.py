from django.shortcuts import render
from library.models import Book
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from writersjam.models import Submission, Prompt
from django.core import serializers
from django.contrib.auth.decorators import login_required
import datetime
from forum.forms import DiscussionForm
from forum.models import Discussion

# Show main library page.
@login_required(login_url='/login/')
def show_discussion(request):
    description = Discussion.objects.all()
    
    context = {
        'discussion': description,
    }
    return render(request, "forum.html", context)

def show_xml(request):
    description = Discussion.objects.all()
    return HttpResponse(serializers.serialize("xml", description), content_type="application/xml")

def show_json(request):
    description = Discussion.objects.all()
    return HttpResponse(serializers.serialize("json", description), content_type="application/json")

def show_xml_by_id(request, id):
    description = Discussion.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", description), content_type="application/xml")

def show_json_by_id(request, id):
    description = Discussion.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", description), content_type="application/json")

def get_discussion_json(request):
    # current_week = datetime.date.today().isocalendar()[1]
    # prompt = Prompt.objects.get(week=current_week)
    # story = Submission.objects.filter(prompt=prompt)
    description = Discussion.objects.all()
    return HttpResponse(serializers.serialize('json', description))

@csrf_exempt
def submit_discussion_ajax(request):
    if request.method == 'POST':
        description = request.POST.get("description")
        date = datetime.datetime.now()
        user = request.user
        username = request.user.username

        new_discussion = Discussion(description=description, date=date, user=user, username=username)
        new_discussion.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()