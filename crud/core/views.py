from django.shortcuts import render

from crud.core.forms import PeopleForm
from crud.core.models import People
from django.shortcuts import redirect


def home(request, pk=None):
    list_of_people = People.objects.all().order_by('-id')
    if request.method == 'POST':
        if pk:
            people = People.objects.get(pk=pk)
            form = PeopleForm(data=request.POST, instance=people)
        else:
            form = PeopleForm(data=request.POST)

        if form.is_valid():
            form.save()
            form = PeopleForm()
    else:
        if pk:
            people = People.objects.get(pk=pk)
            form = PeopleForm(instance=people)
        else:
            form = PeopleForm()

    context = {'form': form, 'peoples': list_of_people}
    return render(request, 'index.html', context)


def remove(request, pk):
    if request.method == 'GET':
        People.objects.filter(pk=pk).delete()
    return redirect('/')
