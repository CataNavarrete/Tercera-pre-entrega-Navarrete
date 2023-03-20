from django.shortcuts import render
from .models import TVSeries
from .forms import TVSeriesForm

def index(request):
    if request.method == 'POST':
        form = TVSeriesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TVSeriesForm()

    series = TVSeries.objects.all()

    context = {
        'form': form,
        'series': series,
    }

    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        form = TVSeriesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TVSeriesForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def search(request):
    query = request.GET.get('q')
    if query:
        series = TVSeries.objects.filter(title__icontains=query)
    else:
        series = TVSeries.objects.all()

    context = {
        'series': series,
        'query': query,
    }

    return render(request, 'search.html', context)
