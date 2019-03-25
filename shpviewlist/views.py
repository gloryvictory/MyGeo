from django.shortcuts import render
from compdata.models import CompData


def shpviewlist(request):
    data = CompData.objects.all()
    return render(request, 'shpviewlist.html', {'data': data})
