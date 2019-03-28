from django.shortcuts import render
from compdata.models import CompData
from hurry.filesize import size
from hurry.filesize import alternative


def shpviewlist(request):
    table_data = []
    shp_files = CompData.objects.filter(extension__endswith='shp')
    for shp_file in shp_files:
        tmp_data = {'shp': 1}
        is_shx = 0
        is_prj = 0
        is_dbf = 0
        is_shpxml = 0
        shx_size = 0
        prj_size = 0
        dbf_size = 0
        shpxml_size = 0
        shp_folder = CompData.objects.filter(folder=shp_file.folder).filter(filename=shp_file.filename)
        for shp_folder_file in shp_folder:
            if shp_folder_file.extension == '.shx':
                is_shx = 1
                shx_size = shp_folder_file.filesize
            if shp_folder_file.extension == '.prj':
                is_prj = 1
                prj_size = shp_folder_file.filesize
            if shp_folder_file.extension == '.dbf':
                is_dbf = 1
                dbf_size = shp_folder_file.filesize
            if shp_folder_file.extension == '.xml':
                is_shpxml = 1
                shpxml_size = shp_folder_file.filesize

        """
        shx_check = CompData.objects.filter(folder=shp_file.folder).filter(filename=shp_file.filename)\
                                    .filter(extension__endswith='shx')
        if shx_check:
            tmp_data['shx'] = 1
        else:
            tmp_data['shx'] = 0

        prj_check = CompData.objects.filter(folder=shp_file.folder).filter(filename=shp_file.filename) \
                                    .filter(extension__endswith='prj')

        if prj_check:
            tmp_data['prj'] = 1
        else:
            tmp_data['prj'] = 0
        """
        if is_shx:
            tmp_data['shx'] = 1
        else:
            tmp_data['shx'] = 0
        if is_prj:
            tmp_data['prj'] = 1
        else:
            tmp_data['prj'] = 0
        if is_dbf:
            tmp_data['dbf'] = 1
        else:
            tmp_data['dbf'] = 0
        if is_shpxml:
            tmp_data['shpxml'] = 1
        else:
            tmp_data['shpxml'] = 0

        tmp_data['compname'] = shp_file.compname
        tmp_data['filename'] = shp_file.filename
        tmp_data['sum_good'] = size(shp_file.filesize + shx_size + prj_size + dbf_size + shpxml_size, system=alternative)
        table_data.append(tmp_data)
        print(tmp_data)

    return render(request, 'shpviewlist.html', {'data': table_data})
