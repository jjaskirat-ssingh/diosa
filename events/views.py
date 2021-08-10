from django.shortcuts import get_object_or_404, render

from .models import Event

def index(request):
    events =  Event.objects.order_by('-event_date').filter(display=True)

      
    context = {
        'events': events
    }

    return render(request, 'pages/index.html', context) 

def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    context = {
    'event': event
    }

    return render(request, 'events/event.html', context) 