# Create your views here.
from django.views.generic.edit import CreateView, UpdateView

from .models import Volunteer, Event, EventSlot
from .forms import VolunteerForm, UpdateVolunteerForm
from django.core.urlresolvers import reverse
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect

class AddVolunteerView(CreateView):
    model = Volunteer
    template_name = "base/index.html"
    form_class = VolunteerForm
    
    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context["event"] = Event.objects.get(id=1)
        context["volunteers"] = Volunteer.objects.all()
        return context
    
    def get_success_url(self):
        return reverse("volunteer-index")
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('volunteer-update', args=[request.user.id]))
        return CreateView.get(self, request, *args, **kwargs)
    
class UpdateVolunteerView(UpdateView):
    model = Volunteer
    template_name = "base/index.html"
    form_class = UpdateVolunteerForm
    
    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, **kwargs)
        context["event"] = Event.objects.get(id=1)
        context["volunteers"] = Volunteer.objects.all()
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.id != int(kwargs["pk"]):
            return HttpResponseRedirect(reverse('volunteer-index'))
        return UpdateView.dispatch(self, request, *args, **kwargs)
    
class CalendarView(TemplateView):
    template_name = "base/cal.html"
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["event"] = Event.objects.get(id=1)
        context["slots"] = EventSlot.objects.all()
        
        return context