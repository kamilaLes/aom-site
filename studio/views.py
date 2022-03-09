from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView

from .forms import ClientForm
from .models import Classes, Trainer, Client



# Create your views here.

class Index(TemplateView):
    template_name = "studio/index.html"

class ClassesView(ListView):
    template_name = "studio/classes.html"
    model = Classes
    context_object_name = "classes"


class SingleClassesView(DetailView):
    model = Classes
    template_name = "studio/classes-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trainers"] = self.object.trainer.all()
        context["equipment"] = self.object.equipment.all()
        context["categories"] = self.object.category.all()
        return context

class TrainersView(ListView):
    model = Trainer
    template_name = "studio/trainers.html"
    context_object_name = "trainers"
    
class TrainerDetails(DetailView):
    model = Trainer
    template_name = "studio/trainer-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classes"] = self.object.classes_set.all()
        return context

class FormView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = "studio/client-form.html"
    success_url = "/thank-you"

class ThankYouView(TemplateView):
    template_name = "studio/thank-you.html"


