from django.shortcuts import render, redirect
from django.http import Http404
import requests
from tmdbv3api import TV
from tmdbv3api import TMDb
import imdb

ia = imdb.IMDb()
tmdb = TMDb()
tmdb.api_key = '122a9fafd99452516fe83207465ce55d'
img1 = "http://image.tmdb.org/t/p/w500/"
tv = TV()
popular = tv.popular()

li = []
det = []
gen = []
nme = []


for i in popular:
    if i.name:
        name = i.name
    else:
        name = ''
    if i.id:
        ids = i.id
    else:
        ids = ''
    if i.poster_path:
        pp = i.poster_path
    else:
        pp = ''
    if i .overview:
        ow = i.overview
    else:
        ow = ''
    air = ''
    z = [name, air, img1+pp, ow]

    nme.append(ids)
    li.append(z)


cast = []
for i in nme:
    m = tv.details(i)
    name = []
    for i in m.credits['cast']:
        name.append(i['name'])
    name.append('')
    name.append('')
    name.append('')
    name.append('')
    name.append('')
    cast.append(name)


gen = []
for i in nme:
    m = tv.details(i)
    gener = []
    di = []
    for i in m.genres:
        gener.append(i['name'])
    ki = ", ".join(gener)
    di.append(ki)
    gen.append(di)
print(gen)


def trending_tv(request):
    return render(request, 'trending_tv.html', {
        'mn1': li[0][0], 'mn2': li[1][0], 'mn3': li[2][0], 'mn4': li[3][0], 'mn5': li[4][0],
        'mn6': li[5][0], 'mn7': li[6][0], 'mn8': li[7][0], 'mn9': li[8][0], 'mn10': li[9][0],
        'mn11': li[10][0], 'mn12': li[11][0], 'mn13': li[12][0], 'mn14': li[13][0], 'mn15': li[14][0],
        'mn16': li[15][0], 'mn17': li[16][0], 'mn18': li[17][0], 'mn19': li[18][0], 'mn20': li[19][0],
        'mu1': li[0][2], 'mu2': li[1][2], 'mu3': li[2][2], 'mu4': li[3][2], 'mu5': li[4][2],
        'mu6': li[5][2], 'mu7': li[6][2], 'mu8': li[7][2], 'mu9': li[8][2], 'mu10': li[9][2],
        'mu11': li[10][2], 'mu12': li[11][2], 'mu13': li[12][2], 'mu14': li[13][2], 'mu15': li[14][2],
        'mu16': li[15][2], 'mu17': li[16][2], 'mu18': li[17][2], 'mu19': li[18][2], 'mu20': li[19][2],
        'rd1': li[0][1], 'rd2': li[1][1], 'rd3': li[2][1], 'rd4': li[3][1], 'rd5': li[4][1],
        'rd6': li[5][1], 'rd7': li[6][1], 'rd8': li[8][1], 'rd9': li[8][1], 'rd10': li[9][1],
        'rd11': li[10][1], 'rd12': li[11][1], 'rd13': li[12][1], 'rd14': li[13][1], 'rd15': li[14][1],
        'rd16': li[15][1], 'rd17': li[16][1], 'rd18': li[17][1], 'rd19': li[18][1], 'rd20': li[19][1],
        'd1': li[0][3], 'd2': li[1][3], 'd3': li[2][3], 'd4': li[3][3], 'd5': li[4][3],
        'd6': li[5][3], 'd7': li[6][3], 'd8': li[7][3], 'd9': li[8][3], 'd10': li[9][3],
        'd11': li[10][3], 'd12': li[11][3], 'd13': li[12][3], 'd14': li[13][3], 'd15': li[14][3],
        'd16': li[15][3], 'd17': li[16][3], 'd18': li[17][3], 'd19': li[18][3], 'd20': li[19][3],
        'gen1': gen[0][0], 'gen2': gen[1][0], 'gen3': gen[2][0], 'gen4': gen[3][0], 'gen5': gen[4][0],
        'gen6': gen[5][0], 'gen7': gen[6][0], 'gen8': gen[7][0], 'gen9': gen[8][0], 'gen10': gen[9][0],
        'gen11': gen[10][0], 'gen12': gen[11][0], 'gen13': gen[12][0], 'gen14': gen[13][0], 'gen15': gen[14][0],
        'gen16': gen[15][0], 'gen17': gen[16][0], 'gen18': gen[17][0], 'gen19': gen[18][0], 'gen20': gen[19][0],
        'cast1': cast[0][0], 'cast2': cast[0][1], 'cast3': cast[0][2], 'cast4': cast[0][3], 'cast5': cast[0][4],
        'cast6': cast[1][0], 'cast7': cast[1][1], 'cast8': cast[1][2], 'cast9': cast[1][3], 'cast10': cast[1][4],
        'cast11': cast[2][0], 'cast12': cast[2][1], 'cast13': cast[2][2], 'cast14': cast[2][3], 'cast15': cast[2][4],
        'cast16': cast[3][0], 'cast17': cast[3][1], 'cast18': cast[3][2], 'cast19': cast[3][3], 'cast20': cast[3][4],
        'cast21': cast[4][0], 'cast22': cast[4][1], 'cast23': cast[4][2], 'cast24': cast[4][3], 'cast25': cast[4][4],
        'cast26': cast[5][0], 'cast27': cast[5][1], 'cast28': cast[5][2], 'cast29': cast[5][3], 'cast30': cast[5][4],
        'cast31': cast[6][0], 'cast32': cast[6][1], 'cast33': cast[6][2], 'cast34': cast[6][3], 'cast35': cast[6][4],
        'cast36': cast[7][0], 'cast37': cast[7][1], 'cast38': cast[7][2], 'cast39': cast[7][3], 'cast40': cast[7][4],
        'cast41': cast[8][0], 'cast42': cast[8][1], 'cast43': cast[8][2], 'cast44': cast[8][3], 'cast45': cast[8][4],
        'cast46': cast[9][0], 'cast47': cast[9][1], 'cast48': cast[9][2], 'cast49': cast[9][3], 'cast50': cast[9][4],
        'cast51': cast[10][0], 'cast52': cast[10][1], 'cast53': cast[10][2], 'cast54': cast[10][3], 'cast55': cast[10][4],
        'cast56': cast[11][0], 'cast57': cast[11][1], 'cast58': cast[11][2], 'cast59': cast[11][3], 'cast60': cast[11][4],
        'cast61': cast[12][0], 'cast62': cast[12][1], 'cast63': cast[12][2], 'cast64': cast[12][3], 'cast65': cast[12][4],
        'cast66': cast[13][0], 'cast67': cast[13][1], 'cast68': cast[13][2], 'cast69': cast[13][3], 'cast70': cast[12][4],
        'cast71': cast[14][0], 'cast72': cast[14][1], 'cast73': cast[14][2], 'cast74': cast[14][3], 'cast75': cast[14][4],
        'cast76': cast[15][0], 'cast77': cast[15][1], 'cast78': cast[15][2], 'cast79': cast[15][3], 'cast80': cast[15][4],
        'cast81': cast[16][0], 'cast82': cast[16][1], 'cast83': cast[16][2], 'cast84': cast[16][3], 'cast85': cast[16][4],
        'cast86': cast[17][0], 'cast87': cast[17][1], 'cast88': cast[17][2], 'cast89': cast[17][3], 'cast90': cast[17][4],
        'cast91': cast[18][0], 'cast92': cast[18][1], 'cast98': cast[18][2], 'cast94': cast[18][3], 'cast95': cast[18][4],
        'cast96': cast[19][0], 'cast97': cast[19][1], 'cast98': cast[19][2], 'cast99': cast[19][3], 'cast100': cast[19][4],
    })
