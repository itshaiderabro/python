import json 
import sys 
import requests 



responde = requests.get("https://mkvcinemas.foo/the-lion-king-2019-movie-brrip-dual-audio-hindi-eng-300mb-480p-1gb-720p-a/")
print(responde.json())