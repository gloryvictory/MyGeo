from django.shortcuts import render
from .forms import UploadForm
from .models import UploadFile
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import time


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            # file = UploadFile()
            # file.file = form.cleaned_data["file"]
            # file.save()
            data = request.FILES['file']
            default_storage.save('tmp/' + time.strftime('%Y-%m-%d-%H-%M-%S') + '_' + str(data), ContentFile(data.read()))
            # return HttpResponseRedirect('/upload/success')
            return render(request, 'upload_success.html', {})
    else:
            form = UploadForm()
    return render(request, 'upload_file.html', {'form': form})

# def handle_uploaded_file(file):
    # default_storage.save()
