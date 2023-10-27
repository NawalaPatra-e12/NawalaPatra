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


@login_required(login_url='/login/')
def create_discussion(request):
    form = DiscussionForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('forum:show_discussion'))

    context = {'form': form}
    return render(request, "create_discussion.html", context)

# Show main library page.
def show_discussion(request):
    data = Discussion.objects.all()
    
    context = {
        'discussion': data,
    }
    return render(request, "forum.html", context)


def show_xml(request):
    data = Discussion.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Discussion.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Discussion.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Discussion.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
