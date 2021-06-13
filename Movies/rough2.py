import requests

url = "https://imdb8.p.rapidapi.com/actors/get-bio"

querystring = {"nconst": "nm0001667"}

headers = {
    'x-rapidapi-key': "e7f0740f9bmsh309f0b26c53ece4p1485adjsnf1062b72cdd5",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
