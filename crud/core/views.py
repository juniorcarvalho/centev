from django.shortcuts import render

from crud.core.forms import PeopleForm
from crud.core.models import People


def home(request):
    list_of_people = People.objects.all().order_by('-id')
    if request.method == 'POST':
        form = PeopleForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = PeopleForm()
    else:
        form = PeopleForm()
    context = {'form': form, 'peoples': list_of_people}
    return render(request, 'index.html', context)
