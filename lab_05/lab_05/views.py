from django.http import HttpResponse
from django.shortcuts import render
import json


def index(request):
    return HttpResponse("Hello, world!")


def indexRender(request):
    return render(request, 'index.html', {})


def universityInfoRender(request):
    js = json.load(open('lab_05/json_data.json', encoding='utf8'))
    f_count = 0
    p_count = 0
    st_count = 0
    mf_count = len(js['university']['scienceDivisions'][0]['megaFaculty'])
    for i in js['university']['scienceDivisions'][0]['megaFaculty']:
        f_count += len(i['faculties'])
        for j in i['faculties']:
            p_count += len(j['pulpits'])
            for p in j['pulpits']:
                for e in p['educationProgrammes']:
                    for g in e['groups']:
                        st_count += len(g['students'])

    return render(request, 'universityInfo.html',
                  {'src': js, 'f_count': f_count, 'p_count': p_count, 'mf_count': mf_count, 'st_count': st_count})


def disciplineInfoRender(request):
    js = json.load(open('lab_05/json_data.json', encoding='utf8'))
    return render(request, 'disciplineInfo.html', {'src': js})


def groupsInfoRender(request):
    js = json.load(open('lab_05/json_data.json', encoding='utf8'))
    return render(request, 'groupsInfo.html', {'src': js})


def departmentsInfoRender(request):
    js = json.load(open('lab_05/json_data.json', encoding='utf8'))
    return render(request, 'departmentsInfo.html', {'src': js})


def universityStructureRender(request):
    js = json.load(open('lab_05/json_data.json', encoding='utf8'))
    return render(request, 'universityStructure.html', {'src': js})
