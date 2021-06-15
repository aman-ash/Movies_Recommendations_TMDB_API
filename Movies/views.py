from django.shortcuts import render, redirect
from django.http import Http404
import requests
from Movies.models import Contact
from tmdbv3api import Movie, Person
from tmdbv3api import TMDb
import imdb

ia = imdb.IMDb()
tmdb = TMDb()
person = Person()
tmdb.api_key = '122a9fafd99452516fe83207465ce55d'
img = "http://image.tmdb.org/t/p/w185/"

movie = Movie()

recommendations = movie.recommendations(19995)


def home(request):

    return render(request, 'home.html')


def test(request):
    return render(request, 'api.html')


def contact(request):
    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        desc = request.POST['desc']
        #print(name, email, phone, desc)
        ins = Contact(name=name, number=number, email=email, desc=desc)
        ins.save()
        print("the data has been written inside the database")

    return render(request, 'contact.html')


def result(request):
    movie_user_likes = request.GET['movie']
    search = movie.search(movie_user_likes)
    a = []
    b = []
    try:
        for res in search:
            a.append(res.id)
            a.append(res.title)
            a.append(res.poster_path)
            b.append(res.overview)

        similar = movie.similar(a[0])
        m = movie.details(a[0])
        gener = []
        gi = []
        di = []
        for i in m.genres:
            gener.append(i['name'])
        ki = ", ".join(gener)
        gi.append(ki)
        cast = []
        k = 0
        for i in m.casts['cast']:
            nme = i['name']
            if i['profile_path'] == None:
                pp = "https://bitslog.files.wordpress.com/2013/01/unknown-person1.gif"
            else:
                pp = img+i['profile_path']
            if i['character'] == None:
                pass
            else:
                char = i['character']
            a_id = i['id']

            z = [nme, pp, char, a_id]
            cast.append(z)
            k += 1
            if k > 7:
                break

        x = []
        y = []
        for i in range(len(cast)):
            x.append(cast[i][3])
        for element in x:
            p = person.details(element)
            y.append(p.biography[:900])
        actor1 = cast[0]
        actor2 = cast[1]
        actor3 = cast[2]
        actor4 = cast[3]
        actor5 = cast[4]
        actor6 = cast[5]
        actor7 = cast[6]
        actor8 = cast[7]
        di.append(m.release_date)
        Recommended_movies_names = []
        Recommended_movies_poster = []
        Recommended_movies_disc = []

        for result in similar:
            Recommended_movies_names.append(result.title)
            Recommended_movies_poster.append(result.poster_path)
            Recommended_movies_disc.append(result.overview)

    # 1st movie details
        id1 = []
        search_new1 = movie.search(Recommended_movies_names[0])
        for res in search_new1:
            id1.append(res.id)
        m1 = movie.details(id1[0])
        gener1 = []
        gi1 = []
        di1 = []
        for i in m1.genres:
            gener1.append(i['name'])
            ki1 = ", ".join(gener1)
            gi1.append(ki1)
            di1.append(m1.release_date)
        cast1 = []
        for i in m1.casts['cast']:
            nme1 = i['name']
            char1 = i['character']
            z1 = [nme1, char1]
            cast1.append(z1)
        gen1 = gi1[-1]
        rd1 = di1[-1]

    # 2nd movie details
        id2 = []
        search_new2 = movie.search(Recommended_movies_names[1])
        for res2 in search_new2:
            id2.append(res2.id)
        m2 = movie.details(id2[0])
        gener2 = []
        gi2 = []
        di2 = []
        for i in m2.genres:
            gener2.append(i['name'])
            ki2 = ", ".join(gener2)
            gi2.append(ki2)
            di2.append(m1.release_date)
        cast2 = []
        for i in m2.casts['cast']:
            nme2 = i['name']
            char2 = i['character']
            z2 = [nme2, char2]
            cast2.append(z2)
        gen2 = gi2[-1]
        rd2 = di2[-1]

    # 3rd movie details
        id3 = []
        search_new3 = movie.search(Recommended_movies_names[2])
        for res3 in search_new3:
            id3.append(res3.id)
        m3 = movie.details(id3[0])
        gener3 = []
        gi3 = []
        di3 = []
        for i in m3.genres:
            gener3.append(i['name'])
            ki3 = ", ".join(gener3)
            gi3.append(ki3)
            di3.append(m3.release_date)
        cast3 = []
        for i in m3.casts['cast']:
            nme3 = i['name']
            char3 = i['character']
            z3 = [nme3, char3]
            cast3.append(z3)
        gen3 = gi3[-1]
        rd3 = di3[-1]

    # 4th movie details
        id4 = []
        search_new4 = movie.search(Recommended_movies_names[3])
        for res4 in search_new4:
            id4.append(res4.id)
        m4 = movie.details(id4[0])
        gener4 = []
        gi4 = []
        di4 = []
        for i in m4.genres:
            gener4.append(i['name'])
            ki4 = ", ".join(gener4)
            gi4.append(ki4)
            di4.append(m4.release_date)
        cast4 = []
        for i in m4.casts['cast']:
            nme4 = i['name']
            char4 = i['character']
            z4 = [nme4, char4]
            cast4.append(z4)
        gen4 = gi4[-1]
        rd4 = di4[-1]

    # 5th movie details
        id5 = []
        search_new5 = movie.search(Recommended_movies_names[4])
        for res5 in search_new5:
            id5.append(res5.id)
        m5 = movie.details(id5[0])
        gener5 = []
        gi5 = []
        di5 = []
        for i in m5.genres:
            gener5.append(i['name'])
            ki5 = ", ".join(gener5)
            gi5.append(ki5)
            di5.append(m5.release_date)
        cast5 = []
        for i in m5.casts['cast']:
            nme5 = i['name']
            char5 = i['character']
            z5 = [nme5, char5]
            cast5.append(z5)
        gen5 = gi5[-1]
        rd5 = di5[-1]

    # 6th movie details
        id6 = []
        search_new6 = movie.search(Recommended_movies_names[5])
        for res6 in search_new6:
            id6.append(res6.id)
        m6 = movie.details(id6[0])
        gener6 = []
        gi6 = []
        di6 = []
        for i in m6.genres:
            gener6.append(i['name'])
            ki6 = ", ".join(gener6)
            gi6.append(ki6)
            di6.append(m6.release_date)
        cast6 = []
        for i in m6.casts['cast']:
            nme6 = i['name']
            char6 = i['character']
            z6 = [nme6, char6]
            cast6.append(z6)
        gen6 = gi6[-1]
        rd6 = di6[-1]

    # 7th movie details
        id7 = []
        search_new7 = movie.search(Recommended_movies_names[6])
        for res7 in search_new7:
            id7.append(res7.id)
        m7 = movie.details(id7[0])
        gener7 = []
        gi7 = []
        di7 = []
        for i in m7.genres:
            gener7.append(i['name'])
            ki7 = ", ".join(gener7)
            gi7.append(ki7)
            di7.append(m7.release_date)
        cast7 = []
        for i in m7.casts['cast']:
            nme7 = i['name']
            char7 = i['character']
            z7 = [nme7, char7]
            cast7.append(z7)
        gen7 = gi7[-1]
        rd7 = di7[-1]

    # 8th movie details
        id8 = []
        search_new8 = movie.search(Recommended_movies_names[7])
        for res8 in search_new8:
            id8.append(res8.id)
        m8 = movie.details(id8[0])
        gener8 = []
        gi8 = []
        di8 = []
        for i in m8.genres:
            gener8.append(i['name'])
            ki8 = ", ".join(gener8)
            gi8.append(ki8)
            di8.append(m8.release_date)
        cast8 = []
        for i in m8.casts['cast']:
            nme8 = i['name']
            char8 = i['character']
            z8 = [nme8, char8]
            cast8.append(z8)
        gen8 = gi8[-1]
        rd8 = di8[-1]

    # 9th movie details
        id9 = []
        search_new9 = movie.search(Recommended_movies_names[8])
        for res9 in search_new9:
            id9.append(res9.id)
        m9 = movie.details(id9[0])
        gener9 = []
        gi9 = []
        di9 = []
        for i in m9.genres:
            gener9.append(i['name'])
            ki9 = ", ".join(gener9)
            gi9.append(ki9)
            di9.append(m9.release_date)
        cast9 = []
        for i in m9.casts['cast']:
            nme9 = i['name']
            char9 = i['character']
            z9 = [nme9, char9]
            cast9.append(z9)
        gen9 = gi9[-1]
        rd9 = di9[-1]

    # 10th movie details
        id10 = []
        search_new10 = movie.search(Recommended_movies_names[9])
        for res10 in search_new10:
            id10.append(res10.id)
        m10 = movie.details(id10[0])
        gener10 = []
        gi10 = []
        di10 = []
        for i in m10.genres:
            gener10.append(i['name'])
            ki10 = ", ".join(gener10)
            gi10.append(ki10)
            di10.append(m10.release_date)
        cast10 = []
        for i in m10.casts['cast']:
            nme10 = i['name']
            char10 = i['character']
            z10 = [nme10, char10]
            cast10.append(z10)
        gen10 = gi10[-1]
        rd10 = di10[-1]

    # 11th movie details
        id11 = []
        search_new11 = movie.search(Recommended_movies_names[10])
        for res11 in search_new11:
            id11.append(res11.id)
        m11 = movie.details(id11[0])
        gener11 = []
        gi11 = []
        di11 = []
        for i in m11.genres:
            gener11.append(i['name'])
            ki11 = ", ".join(gener11)
            gi11.append(ki11)
            di11.append(m11.release_date)
        cast11 = []
        for i in m11.casts['cast']:
            nme11 = i['name']
            char11 = i['character']
            z11 = [nme11, char11]
            cast11.append(z11)
        gen11 = gi11[-1]
        rd11 = di11[-1]

    # 12th movie details
        id12 = []
        search_new12 = movie.search(Recommended_movies_names[11])
        for res12 in search_new12:
            id12.append(res12.id)
        m12 = movie.details(id12[0])
        gener12 = []
        gi12 = []
        di12 = []
        for i in m12.genres:
            gener12.append(i['name'])
            ki12 = ", ".join(gener12)
            gi12.append(ki12)
            di12.append(m12.release_date)
        cast12 = []
        for i in m12.casts['cast']:
            nme12 = i['name']
            char12 = i['character']
            z12 = [nme12, char12]
            cast12.append(z12)
        gen12 = gi12[-1]
        rd12 = di12[-1]

    # 13th movie details
        id13 = []
        search_new13 = movie.search(Recommended_movies_names[12])
        for res13 in search_new13:
            id13.append(res13.id)
        m13 = movie.details(id13[0])
        gener13 = []
        gi13 = []
        di13 = []
        for i in m13.genres:
            gener13.append(i['name'])
            ki13 = ", ".join(gener13)
            gi13.append(ki13)
            di13.append(m13.release_date)
        cast13 = []
        for i in m13.casts['cast']:
            nme13 = i['name']
            char13 = i['character']
            z13 = [nme13, char13]
            cast13.append(z13)
        gen13 = gi13[-1]
        rd13 = di13[-1]

    # 14th movie details
        id14 = []
        search_new14 = movie.search(Recommended_movies_names[13])
        for res14 in search_new14:
            id14.append(res14.id)
        m14 = movie.details(id14[0])
        gener14 = []
        gi14 = []
        di14 = []
        for i in m14.genres:
            gener14.append(i['name'])
            ki14 = ", ".join(gener14)
            gi14.append(ki14)
            di14.append(m14.release_date)
        cast14 = []
        for i in m14.casts['cast']:
            nme14 = i['name']
            char14 = i['character']
            z14 = [nme14, char14]
            cast14.append(z14)
        gen14 = gi14[-1]
        rd14 = di14[-1]

    # 15th movie details
        id15 = []
        search_new15 = movie.search(Recommended_movies_names[14])
        for res15 in search_new15:
            id15.append(res15.id)
        m15 = movie.details(id15[0])
        gener15 = []
        gi15 = []
        di15 = []
        for i in m15.genres:
            gener15.append(i['name'])
            ki15 = ", ".join(gener15)
            gi15.append(ki15)
            di15.append(m15.release_date)
        cast15 = []
        for i in m15.casts['cast']:
            nme15 = i['name']
            char15 = i['character']
            z15 = [nme15, char15]
            cast15.append(z15)
        gen15 = gi15[-1]
        rd15 = di15[-1]

    # 15th movie details
        id16 = []
        search_new16 = movie.search(Recommended_movies_names[15])
        for res16 in search_new16:
            id16.append(res16.id)
        m16 = movie.details(id16[0])
        gener16 = []
        gi16 = []
        di16 = []
        for i in m16.genres:
            gener16.append(i['name'])
            ki16 = ", ".join(gener16)
            gi16.append(ki16)
            di16.append(m16.release_date)
        cast16 = []
        for i in m16.casts['cast']:
            nme16 = i['name']
            char16 = i['character']
            z16 = [nme16, char16]
            cast16.append(z16)
        gen16 = gi16[-1]
        rd16 = di16[-1]

        m_n1 = Recommended_movies_names[0]
        m_n2 = Recommended_movies_names[1]
        m_n3 = Recommended_movies_names[2]
        m_n4 = Recommended_movies_names[3]
        m_n5 = Recommended_movies_names[4]
        m_n6 = Recommended_movies_names[5]
        m_n7 = Recommended_movies_names[6]
        m_n8 = Recommended_movies_names[7]
        m_n9 = Recommended_movies_names[8]
        m_n10 = Recommended_movies_names[9]
        m_n11 = Recommended_movies_names[10]
        m_n12 = Recommended_movies_names[11]
        m_n13 = Recommended_movies_names[12]
        m_n14 = Recommended_movies_names[13]
        m_n15 = Recommended_movies_names[14]
        m_n16 = Recommended_movies_names[15]
        url = "https://image.tmdb.org/t/p/w500/"
        m_u1 = url + Recommended_movies_poster[0]
        m_u2 = url + Recommended_movies_poster[1]
        m_u3 = url + Recommended_movies_poster[2]
        m_u4 = url + Recommended_movies_poster[3]
        m_u5 = url + Recommended_movies_poster[4]
        m_u6 = url + Recommended_movies_poster[5]
        m_u7 = url + Recommended_movies_poster[6]
        m_u8 = url + Recommended_movies_poster[7]
        m_u9 = url + Recommended_movies_poster[8]
        m_u10 = url + Recommended_movies_poster[9]
        m_u11 = url + Recommended_movies_poster[10]
        m_u12 = url + Recommended_movies_poster[11]
        m_u13 = url + Recommended_movies_poster[12]
        m_u14 = url + Recommended_movies_poster[13]
        m_u15 = url + Recommended_movies_poster[14]
        m_u16 = url + Recommended_movies_poster[15]
        m_d1 = Recommended_movies_disc[0]
        m_d2 = Recommended_movies_disc[1]
        m_d3 = Recommended_movies_disc[2]
        m_d4 = Recommended_movies_disc[3]
        m_d5 = Recommended_movies_disc[4]
        m_d6 = Recommended_movies_disc[5]
        m_d7 = Recommended_movies_disc[6]
        m_d8 = Recommended_movies_disc[7]
        m_d9 = Recommended_movies_disc[8]
        m_d10 = Recommended_movies_disc[9]
        m_d11 = Recommended_movies_disc[10]
        m_d12 = Recommended_movies_disc[11]
        m_d13 = Recommended_movies_disc[12]
        m_d14 = Recommended_movies_disc[13]
        m_d15 = Recommended_movies_disc[14]
        m_d16 = Recommended_movies_disc[15]

        return render(request, 'results.html', {'mn0': a[1], 'mu0': url+a[2], 'md0': b[1],
                                                'mn1': m_n1, 'mn2': m_n2, 'mn3': m_n3, 'mn4': m_n4,
                                                'mn5': m_n5, 'mn6': m_n6, 'mn7': m_n7, 'mn8': m_n8,
                                                'mn9': m_n9, 'mn10': m_n10, 'mn11': m_n11, 'mn12': m_n12,
                                                'mn13': m_n13, 'mn14': m_n14, 'mn15': m_n15, 'mn16': m_n16,
                                                'mu1': m_u1, 'mu2': m_u2, 'mu3': m_u3, 'mu4': m_u4,
                                                'mu5': m_u5, 'mu6': m_u6, 'mu7': m_u7, 'mu8': m_u8,
                                                'mu9': m_u9, 'mu10': m_u10, 'mu11': m_u11, 'mu12': m_u12,
                                                'mu13': m_u13, 'mu14': m_u14, 'mu15': m_u15, 'mu16': m_u16,
                                                'md1': m_d1, 'md2': m_d2, 'md3': m_d3, 'md4': m_d4,
                                                'md5': m_d5, 'md6': m_d6, 'md7': m_d7, 'md8': m_d8,
                                                'md9': m_d9, 'md10': m_d10, 'md': m_d11, 'md12': m_d12,
                                                'md13': m_d13, 'md14': m_d14, 'md15': m_d15, 'md16': m_d16,
                                                'a1': actor1[0], 'a2': actor2[0], 'a3': actor3[0], 'a4': actor4[0],
                                                'a5': actor5[0], 'a6': actor6[0], 'a7': actor7[0], 'a8': actor8[0],
                                                'pp1': cast[0][1], 'pp2': cast[1][1], 'pp3': cast[2][1], 'pp4': cast[3][1],
                                                'pp5': cast[4][1], 'pp6': cast[5][1], 'pp7': cast[6][1], 'pp8': cast[7][1],
                                                'char1': cast[0][2], 'char2': cast[1][2], 'char3': cast[2][2], 'char4': cast[3][2],
                                                'char5': cast[4][2], 'char6': cast[5][2], 'char7': cast[6][2], 'char8': cast[7][2],
                                                'cast1': cast1[0][0], 'cast2': cast1[1][0], 'cast3': cast1[2][0], 'cast4': cast1[3][0], 'cast5': cast1[4][0],
                                                'cast6': cast2[0][0], 'cast7': cast2[1][0],  'cast8': cast[2][0],    'cast9': cast2[3][0], 'cast10': cast2[4][0],
                                                'cast11': cast3[0][0], 'cast12': cast3[1][0], 'cast13': cast3[2][0],  'cast14': cast3[3][0], 'cast15': cast3[4][0],
                                                'cast16': cast4[0][0], 'cast17': cast4[1][0], 'cast18': cast4[2][0], 'cast19': cast4[3][0], 'cast20': cast4[4][0],
                                                'cast21': cast5[0][0], 'cast22': cast5[1][0], 'cast23': cast5[2][0], 'cast24': cast5[3][0], 'cast25': cast5[4][0],
                                                'cast26': cast6[0][0], 'cast27': cast6[1][0], 'cast28': cast6[2][0], 'cast29': cast6[3][0], 'cast30': cast6[4][0],
                                                'cast31': cast7[0][0], 'cast32': cast7[1][0], 'cast33': cast7[2][0], 'cast34': cast7[3][0], 'cast35': cast7[4][0],
                                                'cast36': cast8[0][0], 'cast37': cast8[1][0], 'cast38': cast8[2][0], 'cast39': cast8[3][0], 'cast40': cast8[4][0],
                                                'cast41': cast9[0][0], 'cast42': cast9[1][0], 'cast43': cast9[2][0], 'cast44': cast9[3][0], 'cast45': cast9[4][0],
                                                'cast46': cast10[0][0], 'cast47': cast10[1][0], 'cast48': cast10[2][0], 'cast49': cast10[3][0], 'cast50': cast10[4][0],
                                                'cast51': cast11[0][0], 'cast52': cast11[1][0], 'cast53': cast11[2][0], 'cast54': cast11[3][0], 'cast55': cast11[4][0],
                                                'cast56': cast12[0][0], 'cast57': cast12[1][0], 'cast58': cast12[2][0], 'cast59': cast12[3][0], 'cast60': cast12[4][0],
                                                'cast61': cast13[0][0], 'cast62': cast13[1][0], 'cast63': cast13[2][0], 'cast64': cast13[3][0], 'cast65': cast13[4][0],
                                                'cast66': cast14[0][0], 'cast67': cast14[1][0], 'cast68': cast14[2][0], 'cast69': cast14[3][0], 'cast70': cast14[4][0],
                                                'cast71': cast15[0][0], 'cast72': cast15[1][0], 'cast73': cast15[2][0], 'cast74': cast15[3][0], 'cast75': cast15[4][0],
                                                'cast76': cast16[0][0], 'cast77': cast16[1][0], 'cast78': cast16[2][0], 'cast79': cast16[3][0], 'cast80': cast16[4][0],
                                                'date': di[-1], 'gener': gi[-1],
                                                'gen1': gen1, 'rd1': rd1, 'gen2': gen2, 'rd2': rd2,
                                                'gen3': gen3, 'rd3': rd3, 'gen4': gen4, 'rd4': rd4,
                                                'gen5': gen5, 'rd5': rd5, 'gen6': gen6, 'rd6': rd6,
                                                'gen7': gen7, 'rd7': rd7, 'gen8': gen8, 'rd8': rd8,
                                                'gen9': gen9, 'rd9': rd9, 'gen10': gen10, 'rd10': rd10,
                                                'gen11': gen11, 'rd11': rd11, 'gen12': gen12, 'rd12': rd12,
                                                'gen13': gen13, 'rd13': rd13, 'gen14': gen14, 'rd14': rd14,
                                                'gen15': gen15, 'rd15': rd15, 'gen116': gen16, 'rd16': rd16,
                                                'bio1': y[0], 'bio2': y[1], 'bio3': y[2], 'bio4': y[3],
                                                'bio5': y[4], 'bio6': y[5], 'bio7': y[6], 'bio8': y[7]

                                                })

    except:
        return render(request, 'home.html', {'not_found': 'Please Check The Spelling'})
