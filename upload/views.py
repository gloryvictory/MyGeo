from django.shortcuts import render
from .forms import UploadForm
from compdata.models import CompData
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import time
import csv
import os
from pathlib import Path
import logging
from django.utils import timezone


csv.register_dialect('myCSV', delimiter=';', quoting=csv.QUOTE_ALL, skipinitialspace=True)
logger = logging.getLogger(__name__)


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            # file = UploadFile()
            # file.file = form.cleaned_data["file"]
            # file.save()
            data = request.FILES['file']
            filename = time.strftime('%Y-%m-%d-%H-%M-%S') + '_' + str(data)
            default_storage.save('tmp/' + filename, ContentFile(data.read()))
            with open('tmp/' + filename, 'r+', encoding='utf-8') as f:
                reader = csv.reader(f, dialect='myCSV')
                i = 0
                for row in reader:
                    if i > 1:
                        computer = row[0]
                        filepath = row[1]
                        filesize = row[2]
                        ctime = row[3]
                        rec = CompData()
                        rec.compname = computer
                        try:
                            rec.filesize = filesize
                        except:
                            logger.error('Wrong file size')
                            pass
                        rec.added = time.strftime('%Y-%m-%d %H:%M:%S')
                        rec.created = time.strftime('%Y-%m-%d %H:%M:%S')
                        rec.fullname = filepath
                        rec.extension = Path(row[1]).suffix
                        rec.folder = os.path.dirname(row[1])
                        rec.disk = row[1][0]
                        basename = os.path.basename(row[1])
                        rec.filename = os.path.splitext(basename)[0]
                        rec.save()
                    i = i + 1

                    pass
            # rec = CompData()
            f.close()
            return render(request, 'upload_success.html', {})
    else:
            form = UploadForm()
    return render(request, 'upload_file.html', {'form': form})

# def handle_uploaded_file(file):
