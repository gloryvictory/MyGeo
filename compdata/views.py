from django.shortcuts import render
from .models import CompData


def comp_list_view(request):
    compdata = CompData.objects.all()
    return render(request, 'comp_list_view.html', {'compdata': compdata})
