import pandas as pd
import numpy as np
import imdb as im
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

cv=CountVectorizer()
data=pd.read_csv("movie.csv")
cm=cv.fit_transform(data["combine"])

def suggetion(mvnm):
    ind=data[data.original_title==mvnm]["index"].values[0]
    relate=pd.DataFrame(list(enumerate(cosine_similarity(cm)[ind])))
    relate["accuracy"]=relate.iloc[:][1]
    lp=data[relate.accuracy>0.28]["index"].to_numpy()
    li=[]
    for i in lp:
        li.append(data[data.index==i]["id"].values[0])
        # print(data[data.index==i]["original_title"].values[0])
    return im.detailsofsuggetionmovies(li)

def moviename(mvnm):
    movieidmb=data[data.original_title==mvnm]["id"].values[0]
    return im.gvnmovie(movieidmb)


if __name__=='__main__':
    # suggetion("Red Planet")
    print(moviename("The Avengers")[0])
    
    # print("succesfully executed")
    # pass