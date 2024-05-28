import requests

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages

from persons.models import Skills, Persons
from persons.forms import NameForm


def main(request):
    return render(request, template_name="main.html")


class SkillList(ListView):
    queryset = Skills.objects.prefetch_related('persons_set__position')
    template_name = "skills.html"
    context_object_name = "skills"


def persons(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            selected_name = form.cleaned_data['first_name']

            url = f"https://api.agify.io/?name={selected_name}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                age = data.get("age")

                Persons.objects.filter(first_name=selected_name).update(age=age)
                persons = Persons.objects.filter(age__isnull=False).distinct().order_by('age')

                return render(request, template_name="persons.html", context={'form': form, 'persons': persons})

            messages.error(request, "Brak odpowiedzi serwera, spróbuj ponownie później")
            return redirect('persons:persons')

    form = NameForm()
    return render(request, template_name="persons.html", context={'form': form})
