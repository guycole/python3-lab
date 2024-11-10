#
# Title: model.py
# Description: 
#
import json

# from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

from model import Album, Artist, Song

class Reporter:
    def reporter(self, album: Album) -> None:
        print(f"Album: {album.title}, {album.release}, {album.format}, {album.genre}, {album.artist.last_name}, {album.artist.first_name}")

        for song in album.songs:
            print(f"Song: {song.title}, {song.file_name}")

        return
    
    def json_manifest(self, album: Album, file_name: str) -> dict[str, any]:
        dd = {}
        dd["version"] = 1
        dd["title"] = album.title
        dd["file-name"] = file_name
        dd["mb-id"] = album.mb_id
        dd["asin"] = album.asin
        dd["duration"] = album.duration
        dd["release"] = album.release
        dd["disc-count"] = album.disc_count
        dd["track-count"] = album.track_count
        dd["note"] = album.note

        if album.format == 'Digital Media':
            dd["format"] = 'DIGITAL_MEDIA'
        else:
            dd["format"] = 'CD'

        dd["genre"] = 'ROCK'

        dd_artist = {}
        if album.artist.last_name == 'Various Artists':
            dd_artist["last-name"] = 'VARIOUS_ARTISTS'
            dd_artist["first-name"] = 'EMPTY_STRING'
        else:
            dd_artist["last-name"] = album.artist.last_name
            dd_artist["first-name"] = album.artist.first_name

        dd_artist["mb-id"] = album.artist.mb_id

        dd["artist"] = dd_artist

        duration_total = 0
        songs = []

        for song in album.songs:
            dd_song = {}
            dd_song["title"] = song.title
            dd_song["file-name"] = song.file_name
            dd_song["mb-id"] = song.mb_id
            dd_song["duration"] = song.duration

            dd_artist = {}
            dd_artist["first-name"] = song.artist.first_name
            dd_artist["last-name"] = song.artist.last_name
            dd_artist["mb-id"] = song.artist.mb_id

            dd_song["artist"] = dd_artist
            
            songs.append(dd_song)

            duration_total += song.duration

        dd["duration"] = duration_total
        dd["songs"] = songs
     
        return dd
    
    def write_json_manifest(self, datum: dict[str, any]) -> None:
        with open("manifest.json", "w") as outfile:
            json.dump(datum, outfile, indent=2)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
