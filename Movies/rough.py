from tmdbv3api import Movie
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '122a9fafd99452516fe83207465ce55d'

img1 = "http://image.tmdb.org/t/p/w200/"
img = "http://image.tmdb.org/t/p/w185/"
movie = Movie()

recommendations = movie.recommendations(19995)


#     print(recommendation.overview)
search = movie.search('titanic')
idi = []
for res in search:
    idi.append(res.id)


movie = Movie()
popular = movie.popular()
m = movie.details(idi[0])
gener = []
gi = []
di = []
for i in m.genres:
    gener.append(i['name'])
    ki = ", ".join(gener)
    gi.append(ki)
    di.append(m.release_date)
# print(di[-1])
# print(gi[-1])
cast = []
for i in m.casts['cast']:
    nme = i['name']
    if(i['profile_path'] == None):
        pp = "https://bitslog.files.wordpress.com/2013/01/unknown-person1.gif"
    else:
        pp = img+i['profile_path']
    char = i['character']
    z = [nme, pp, char]
    cast.append(z)
similar = movie.similar(idi[0])
Recommended_movies_names = []
Recommended_movies_poster = []
Recommended_movies_disc = []
for result in similar:
    Recommended_movies_names.append(result.title)
    Recommended_movies_poster.append(result.poster_path)
    Recommended_movies_disc.append(result.overview)

id1 = []
search_new1 = movie.search(Recommended_movies_names[1])
for res in search_new1:
    id1.append(res.id)

m1 = movie.details(id1[0])

gener1 = []
gi1 = []
di1 = []
for i in m1.genres:
    gener1.append(i['name'])
    ki1 = ", ".join(gener)
    gi1.append(ki1)
    di1.append(m1.release_date)

cast1 = []
for i in m1.casts['cast']:
    nme1 = i['name']

    char1 = i['character']
    z1 = [nme1, char1]
    cast1.append(z1)
m1_t = m1.title
gen1 = gi1[-1]
rd1 = di1[-1]
