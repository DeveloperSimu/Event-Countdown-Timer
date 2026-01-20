# home/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

def home(request):
    events = Event.objects.all().order_by('event_date')

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()

    context = {
        'events': events,
        'form': form
    }
    return render(request, 'myapp.html', context)  # <-- template name ঠিক করতে হবে

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('home')
