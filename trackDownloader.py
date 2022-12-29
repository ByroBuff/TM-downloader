import requests
from bs4 import BeautifulSoup
import os
from urllib import request
import os
import json
import urllib.parse

darkgreen = "\033[32m"
reset = "\033[00m"
link = "\033[34m\033[04m"

DOWNLOAD_URL = "https://tmnf.exchange/trackgbx/"
RANDOM_URL = "https://tmnf.exchange/trackrandom/?"

os.system('cls' if os.name == 'nt' else 'clear')

print(" ")
print(" ")
print(f"   {darkgreen}█▀▄▀█ ▄▀█ █▀ █▀   ▀█▀ █▀█ ▄▀█ █▀▀ █▄▀   █▀▄ █▀█ █ █ █ █▄ █ █   █▀█ ▄▀█ █▀▄ █▀▀ █▀█")
print(f"   {darkgreen}█ ▀ █ █▀█ ▄█ ▄█    █  █▀▄ █▀█ █▄▄ █ █   █▄▀ █▄█ ▀▄▀▄▀ █ ▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄")
print(reset)
print(" ")

directory = ""
while True:
    print(f"   Documentation: {link}https://sites.google.com/view/trackrandom{reset}")
    print(f"   Format: {darkgreen}<parameter>=<value>{reset}")
    param = input("   Parameter (leave blank to continue):")
    if param == "":
        break
    else:
        param, value = param.split("=")
        value = urllib.parse.quote(value).replace("%20", "+")
        RANDOM_URL += f"{param}={value}&"

RANDOM_URL = RANDOM_URL[:-1]


while not os.path.exists(directory):
    directory = input("   Folder of tracks (default: ./tracks): ").strip('"')
    if directory == "":
        directory = "tracks"
        if not os.path.exists("tracks"):
            os.makedirs("tracks")

while True:
    try:
        count = int(input("   How Many tracks: "))
        break
    except ValueError:
        continue

print(" ")

i = 0
while i < count:

    url = RANDOM_URL

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
        continue

    print(f"   ({i + 1}) {darkgreen}Found: {reset}{trackName} {darkgreen}by: {reset}{author}")
    i += 1

print(" ")
input("Finished! Press enter to exit.")