from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from event.forms import *

# Create your views here.
class EventView(generic.ListView):
    model = Event
    template_name = 'event/index.html'
    def index(request):
        event = Event.objects.all()
        likedEvent = Event.objects.filter(is_liked=request.user.id)
        return render(request, 'event/index.html', {'events':event, 'likedEvent':likedEvent})

@login_required(login_url='/login')
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Event Successfully Created")
    else:
        form = EventForm()

    return render(request, 'event/create.html', {'form': form})

@login_required
def likedEvents(request):
    event = Event.objects.filter(is_liked=request.user.id)
    return render(request, 'event/liked.html', {'events':event})

@login_required(login_url='/login')
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('id'))
        event = get_object_or_404(Event, id=id)
        print(event)
        if event.is_liked.filter(id=request.user.id).exists():
            event.is_liked.remove(request.user)
            event.save()
            result = 'unlike'
        else:
            event.is_liked.add(request.user)
            event.save()
            result = 'like'
        return JsonResponse({'result':result})
