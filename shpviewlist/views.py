from django.shortcuts import render
from compdata.models import CompData
from django.db.models import Q


def shpviewlist(request):
    table_data = []
    shp_files = CompData.objects.filter(extension__endswith='shp')
    for shp_file in shp_files:
        tmp_data = {}
        tmp_data['shp'] = 1
        shx_flag = False
        prj_flag = False
        shp_folder = CompData.objects.filter(folder=shp_file.folder)
        for shp_folder_file in shp_folder:
            if shp_folder_file.extension == '.shx':
                tmp_data['shx'] = 1
                shx_flag = True
                print('shx')
            if shp_folder_file.extension == '.prj':
                tmp_data['prg'] = 1
                prj_flag = True
                print('prj')
        table_data.append(tmp_data)

    return render(request, 'shpviewlist.html', {'data': table_data})
