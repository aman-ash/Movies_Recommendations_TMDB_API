from django.shortcuts import render, redirect
from django.http import Http404
import requests
from tmdbv3api import Movie, Person
from tmdbv3api import TMDb
import imdb

ia = imdb.IMDb()
tmdb = TMDb()
tmdb.api_key = '122a9fafd99452516fe83207465ce55d'
img1 = "http://image.tmdb.org/t/p/w200/"
img = "http://image.tmdb.org/t/p/w185/"
movie = Movie()
person = Person()
popular = movie.popular()

li = []
for i in popular:
    li.append(i.title)

id_li = []
idies = []
for element in li:
    search_pop = movie.search(element)
    idies.clear()
    for res in search_pop:
        idies.append(res.id)
        id_li.append(idies[0])

unique_list = []

for x in id_li:
    if x not in unique_list:
        unique_list.append(x)
# print(unique_list)
# print(li)


def trending(request):
    values = []
    kl = []
    vl = []
    for i in unique_list:
        m = movie.details(i)
        if m.poster_path:
            values.append(img1+m.poster_path)
        else:
            values.append(None)

        if m.release_date:
            values.append(m.release_date)
        else:
            values.append(None)
        if m.overview:
            values.append(m.overview)
        else:
            values.append(None)
    kl.append(values)
    final = []
    for i in unique_list:
        m = movie.details(i)
        gener = []
        gi = []
        di = []
        for i in m.genres:
            gener.append(i['name'])
        ki = ", ".join(gener)
        gi.append(ki)
        final.append(gi)
    cast = []
    for i in unique_list:
        m = movie.details(i)
        name = []
        for i in m.casts['cast']:
            if i['name']:
                name.append(i['name'])
            else:
                name.append('')
        name.append('')
        name.append('')
        name.append('')
        name.append('')
        name.append('')
        di.append(name)
        cast.append(name)
    print(cast)

    return render(request, 'trending.html', {
        'mn1': li[0], 'mn2': li[1], 'mn3': li[2], 'mn4': li[3], 'mn5': li[4],
        'mn6': li[5], 'mn7': li[6], 'mn8': li[7], 'mn9': li[8], 'mn10': li[9],
        'mn11': li[10], 'mn12': li[11], 'mn13': li[12], 'mn14': li[13], 'mn15': li[14],
        'mn16': li[15], 'mn17': li[16], 'mn18': li[17], 'mn19': li[18], 'mn20': li[19],
        'mu1': kl[0][0], 'mu2': kl[0][3], 'mu3': kl[0][6], 'mu4': kl[0][9], 'mu5': kl[0][12],
        'mu6': kl[0][15], 'mu7': kl[0][18], 'mu8': kl[0][21], 'mu9': kl[0][24], 'mu10': kl[0][27],
        'mu11': kl[0][30], 'mu12': kl[0][33], 'mu13': kl[0][36], 'mu14': kl[0][39], 'mu15': kl[0][42],
        'mu16': kl[0][45], 'mu17': kl[0][48], 'mu18': kl[0][51], 'mu19': kl[0][54], 'mu20': kl[0][57],
        'rd1': kl[0][1], 'rd2': kl[0][4], 'rd3': kl[0][7], 'rd4': kl[0][10], 'rd5': kl[0][13],
        'rd6': kl[0][16], 'rd7': kl[0][19], 'rd8': kl[0][22], 'rd9': kl[0][25], 'rd10': kl[0][28],
        'rd11': kl[0][31], 'rd12': kl[0][34], 'rd13': kl[0][37], 'rd14': kl[0][40], 'rd15': kl[0][43],
        'rd16': kl[0][46], 'rd17': kl[0][49], 'rd18': kl[0][52], 'rd19': kl[0][55], 'rd20': kl[0][58],
        'd1': kl[0][2], 'd2': kl[0][5], 'd3': kl[0][8], 'd4': kl[0][11], 'd5': kl[0][14],
        'd6': kl[0][17], 'd7': kl[0][20], 'd8': kl[0][23], 'd9': kl[0][26], 'd10': kl[0][29],
        'd11': kl[0][32], 'd12': kl[0][35], 'd13': kl[0][38], 'd14': kl[0][41], 'd15': kl[0][44],
        'd16': kl[0][47], 'd17': kl[0][50], 'd18': kl[0][53], 'd19': kl[0][56], 'd20': kl[0][59],
        'gen1': final[0][0], 'gen2': final[1][0], 'gen3': final[2][0], 'gen4': final[3][0], 'gen5': final[4][0],
        'gen6': final[5][0], 'gen7': final[6][0], 'gen8': final[7][0], 'gen9': final[8][0], 'gen10': final[9][0],
        'gen11': final[10][0], 'gen12': final[11][0], 'gen13': final[12][0], 'gen14': final[13][0], 'gen15': final[14][0],
        'gen16': final[15][0], 'gen17': final[16][0], 'gen18': final[17][0], 'gen19': final[18][0], 'gen20': final[19][0],
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
