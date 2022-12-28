import requests
from bs4 import BeautifulSoup
import os
from urllib import request
import os
import json

darkgreen = "\033[32m"
reset = "\033[00m"

DOWNLOAD_URL = "https://tmnf.exchange/trackgbx/"

os.system('cls' if os.name == 'nt' else 'clear')

print(" ")
print(" ")
print(f"   {darkgreen}█▀▄▀█ ▄▀█ █▀ █▀   ▀█▀ █▀█ ▄▀█ █▀▀ █▄▀   █▀▄ █▀█ █ █ █ █▄ █ █   █▀█ ▄▀█ █▀▄ █▀▀ █▀█")
print(f"   {darkgreen}█ ▀ █ █▀█ ▄█ ▄█    █  █▀▄ █▀█ █▄▄ █ █   █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄")
print(reset)
print(" ")

directory = ""

while not os.path.exists(directory):
    directory = input("   Folder of tracks (default: ./tracks): ").strip('"')
    if directory == "":
        directory = "tracks"

while True:
    try:
        count = int(input("   How Many tracks: "))
        break
    except ValueError:
        continue

print(" ")

i = 0
while i < count:

    url = "https://tmnf.exchange/trackrandom"

    r = requests.get(url)

    soup=BeautifulSoup(r.content,"html.parser")

    trackid = soup.find("a",{"class":"btn btn-primary"}).get("href")[10:]
    trackName = soup.find("div",{"class":"col text-break"}).find("h3").text

    author = json.loads(soup.find("div",{"class":"trackshow-authors"}).find("span").get("template-data"))["Name"]

    name = request.urlopen(request.Request(DOWNLOAD_URL + trackid)).info().get_filename()

    if not os.path.exists(f"{directory}/tracks"):
        os.makedirs(f"{directory}/tracks")

    if not os.path.exists(f"{directory}/links"):
        os.makedirs(f"{directory}/links")

    try:
        with open(f"{directory}/tracks/{name}","wb") as file:
            file.write(requests.get(DOWNLOAD_URL + trackid).content)

        with open(f"{directory}/links/TMX LINKS.txt", "a") as links:
            links.write(f"{trackName} : https://tmnf.exchange/trackshow/{trackid}\n")
    except:
        i -= 1
        continue

    print(f"   ({i + 1}) {darkgreen}Found: {reset}{trackName} {darkgreen}by: {reset}{author}")
    i += 1

print(" ")
input("Finished! Press enter to exit.")