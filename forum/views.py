from django.shortcuts import render, get_object_or_404
from library.models import Book
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from writersjam.models import Submission, Prompt
from django.core import serializers
from django.contrib.auth.decorators import login_required
import datetime
from forum.forms import DiscussionForm, ReplyForm
from forum.models import Discussion, Reply
from django.shortcuts import redirect
from django.http import JsonResponse






# Show main library page.
@login_required(login_url='/login/')
def show_discussion(request):
    description = Discussion.objects.all()
    reply_form = ReplyForm()  # Create an instance of your reply form.

    
    context = {
        'discussion': description,
        'reply_form': reply_form

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


        new_discussion = Discussion(description=description, date=date, user=user)
        new_discussion.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def add_reply(request, discussion_id):
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            discussion = get_object_or_404(Discussion, id=discussion_id)
            new_reply = reply_form.save(commit=False)
            new_reply.discussion = discussion
            new_reply.user = request.user
            new_reply.save()
            return redirect('discussion_detail', discussion_id=discussion_id)
    else:
        reply_form = ReplyForm()

    return render(request, 'forum.html', {'reply_form': reply_form})

def discussion_detail(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    reply_form = ReplyForm()
    replies = Reply.objects.filter(discussion=discussion)

    return render(request, 'forum.html', {'discussion': discussion, 'reply_form': reply_form, 'replies': replies})

def view_replies(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    replies = Reply.objects.filter(discussion=discussion)
    return render(request, 'forum.html', {'discussion': discussion, 'replies': replies})

def get_replies(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    replies = Reply.objects.filter(discussion=discussion)

    # Manually convert model instances to a list of dictionaries
    replies_data = [
        {
            'id': reply.id,
            'text': reply.text,
            'user': reply.user.username,
            'created_at': reply.created_at,
            # Add other fields as needed
        }
        for reply in replies
    ]

    return JsonResponse(replies_data, safe=False)