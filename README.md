# MassTrackDownloader

## Description
This project is a tool for windows meant to automatically download many random tracks from [TMX](https://tmnf.exchange). This tool only works for TMNF (Trackmania Nations Forever) at the moment. The tool can be used for many things including:

- playing user created maps without wifi
- random map competition in which the maps are pre-picked
- Discovering many new trackmania maps

## Installation
<br>

```
git clone https://github.com/ByroBuff/TM-downloader.git

cd TM-downloader

python -m pip install -r requirements.txt

python trackDownloader.py
```

### Alternate method for noobs
1. Download [This](https://github.com/wholeheartedness/TM-downloader/archive/refs/heads/main.zip)
2. Extract zip file
3. Run `packageInstaller.bat`
4. When ready to find tracks run `trackDownloader.py`

## Usage

### General
Upon Start of the program, you will be prompted to enter the directory you want to send the tracks to. Be aware that the tracks are not directly entered into that directory but added into a subfolder called ```tracks``` this is for ease of use because the links to the [TMX](https://tmnf.exchange) page is also stored in a subfolder called ```links```. This is to increase efficiency when browsing. You will also be prompted with the amount of tracks you want to download.

### Parameters

Parameters are modifiers that can be added to the random track search to narrow your search. Some examples of paramters could be the author or the upload date of a track. A full documentation of the parameters can be found at https://sites.google.com/view/trackrandom created by myself for the purposes of this project.

## Important ⚠

#### Tracks With the character ```?``` cannot be downloaded by this program
