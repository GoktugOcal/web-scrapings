import requests
import json
import html

APIKEY = YOUR_KEY
not_found = 0

with open("data/movies.json", "r", encoding="utf8") as f:
    movies = json.loads(f.read())

for movie in movies:
    movie_name = movie["movie_name"]
    print(movie_name)

    address = "http://www.omdbapi.com/?t=" + movie_name + "&apikey="+APIKEY
    response = requests.get(address)
    try:
        if json.loads(response.text)["Response"] == "True":
            info = json.loads(response.text)
            movie["runtime"] = info["Runtime"]
            movie["genre"] = info["Genre"]
            movie["Metascore"] = info["Metascore"]
            movie["imdbRating"] = info["imdbRating"]
        else:
            address = "http://www.omdbapi.com/?t=" + movie["original_name"].replace(" ","+") + "&apikey="+APIKEY
            response = requests.get(address)
            info = json.loads(response.text)
            movie["runtime"] = info["Runtime"]
            movie["genre"] = info["Genre"]
            movie["Metascore"] = info["Metascore"]
            movie["imdbRating"] = info["imdbRating"]
            
    except:
        print(movie_name,"-",movie["original_name"]+"######################")
        not_found += 1



print("Not found:", not_found)

movies

with open("data/movies_detailed.json", "w", encoding='utf8') as f:
    f.write(json.dumps(movies, indent=4))
    print("JSON created...")