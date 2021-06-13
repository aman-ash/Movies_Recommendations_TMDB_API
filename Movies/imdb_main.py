from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
tmdb.api_key = '122a9fafd99452516fe83207465ce55d'

img1="http://image.tmdb.org/t/p/w200/"
img="http://image.tmdb.org/t/p/w185/"
movie = Movie()

def gvnmovie(imdb):
    li=[]
    m = movie.details(imdb)
    li.append(m.title)
    li.append(img1+m.poster_path)
    li.append("Tagline : ")
    li.append(m.tagline)
    li.append("Overview :")
    li.append(m.overview)
    gener=[]
    for i in m.genres:
        gener.append(i['name'])
    ki=", ".join(gener)
    li.append("Gener : ")
    li.append(ki)
    # print(m.release_date)
    li.append("Release Date : ")
    li.append(m.release_date)
    li.append("Status : ")
    li.append(m.status)
    li.append("Rating : ")
    li.append(m.vote_average)
    cast=[]
    k=0
    for i in m.casts['cast']:
        id=i['id']
        nme=i['name']
        if(i['profile_path']==None):
            pp="https://bitslog.files.wordpress.com/2013/01/unknown-person1.gif"
        else:
            pp=img+i['profile_path']
        char=i['character']
        z=[id,nme,pp,char]
        cast.append(z)
        # if k>7:
        #     break
        
    li.append(cast)

    return li;

def detailsofsuggetionmovies(li):
    kl=[]
    for i in li:
        li=[]
        m = movie.details(i)
        # print(m.poster_path)
        li.append(i)
        li.append(m.title)
        li.append(img1+m.poster_path)
        # li.append(m.overview)
        li.append(m.release_date)
        li.append(m.status)
        li.append(m.vote_average)
        kl.append(li)
    return kl;

if __name__=="__main__":
    # print(gvnmovie("299534"))
    pass
