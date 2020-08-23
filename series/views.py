from django.shortcuts import render
from series.models import Series

def series_index(request):
    series = Series.objects.all()
    context = {
        'series':series
    }
    return render(request,'series_index.html',context)

def series_detail(request,pk):
    se = Series.objects.get(pk=pk)
    context = {
        'se':se
    }
    return render(request,'series_detail.html',context)
