from django.shortcuts import render, redirect
from django.views import generic
from .models import Thing
from .forms import CreateThing
from django.views.decorators.http import require_POST
from django.utils.timezone import now

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = "home.html"
    form = CreateThing

    def get(self, request):
        things = Thing.objects.all().order_by("id").values()
        args = {"things": things, "add_thing": self.form}
        return render(request, self.template_name, args)


@require_POST
def add_thing(request):
    form = CreateThing(request.POST)

    if form.is_valid():
        new_thing = Thing(body=request.POST["body"])
        new_thing.save()
        return redirect("home")


def complete_thing(request, thing_id):
    thing = Thing.objects.get(pk=thing_id)
    thing.completed = True
    thing.save()
    return redirect("home")


def delete_completed_things(request):
    Thing.objects.filter(completed=True).delete()
    return redirect("home")
