import imdb
from imdb import IMDb
from tmdbv3api import Movie
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '122a9fafd99452516fe83207465ce55d'


# creating instance of IMDb
ia = imdb.IMDb()

# ID
code = "1187043"

# getting movie
movie = ia.get_movie(code)
gener = []
li = []
m = movie.details(1187043)
for i in m.genres:
    gener.append(i['name'])
ki = ", ".join(gener)
li.append("Gener : ")
li.append(ki)

# printing movie object
print(li)
print(movie.genre)

print("===============")

# getting cast
cast = movie['cast']

# actor name from caste
actor = cast[0]
actor1 = cast[0]
a = actor1
print(actor)
print(actor1)

# role played
role = actor.notes
role1 = actor1.notes

movie = Movie()

recommendations = movie.recommendations(19995)


search = movie.search('Gravity')
a = []
b = []
for res in search:
    a.append(res.id)
    b.append(res.overview)
    a.append(res.title)
    a.append(res.poster_path)
    a.append(res.vote_average)
    a.append(res.popularity)


similar = movie.similar(a[0])
Recommended_movies_names = []
Recommended_movies_poster = []
Recommended_movies_disc = []
for result in similar:
    Recommended_movies_names.append(result.title)
    Recommended_movies_poster.append(result.poster_path)
    Recommended_movies_disc.append(result.overview)


print(b[1])
