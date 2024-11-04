#
# Title: model.py
# Description: 
# 
# from bs4 import BeautifulSoup
import xml.etree.ElementTree as et

class Album:
    def __init__(self):
        self.version = None
        self.title = None
        self.file_name = None
        self.mb_id = None
        self.asin = None
        self.duration = None
        self.release = None
        self.disc_count = None
        self.track_count = None
        self.active = True
        self.note = None
        self.format = None
        self.genre = None
        self.artist = None
        self.songs = []

    def __str__(self) -> str:
        return(f"Album: {self.title}, {self.file_name}, {self.mb_id}")

class Artist:
    def __init__(self, last_name: str, first_name: str, mb_id: str):
        self.last_name = last_name
        self.first_name = first_name
        self.mb_id = mb_id

    def __str__(self) -> str:
       return f"Artist: {self.last_name}, {self.first_name}, {self.mb_id}"

class Song:
    def __init__(self, title: str, file_name: str, mb_id: str, duration: int):
        self.title = title
        self.file_name = file_name
        self.mb_id = mb_id
        self.duration = duration

    def __str__(self) -> str:
        return f"Song: {self.title}, {self.duration}, {self.file_name}, {self.mb_id}"

class Parser:

    def single_element(self, root, key:str) -> str:
        for temp in root.findall(key):
            return temp.text

        return None
    
    def get_artist(self, root) -> Artist:
        last_name = self.single_element(root, "last_name")
        first_name = self.single_element(root, "first_name")
        mb_id = self.single_element(root, "mb_id")
        return Artist(last_name, first_name, mb_id)

    def get_song(self, root) -> Song:
        title = self.single_element(root, "title")
        file_name = self.single_element(root, "file_name")
        mb_id = self.single_element(root, "mb_id")
        duration = int(self.single_element(root, "duration"))
        song = Song(title, file_name, mb_id, duration)
        song.disk = int(self.single_element(root, "disc"))
        song.track = int(self.single_element(root, "track"))
        song.active = self.single_element(root, "active")
        song.note = self.single_element(root, "note")

        song.artist = None
        for temp in root.findall('artist'):
            song.artist = self.get_artist(temp)
        
        return song

    def reader(self, file_name: str) -> Album:
        album = Album()

        tree = et.parse(file_name)
        root = tree.getroot()

        album.version = self.single_element(root, "version")
        album.title = self.single_element(root, "title")
        album.file_name = self.single_element(root, "file_name")
        album.mb_id = self.single_element(root, "mb_id")
        album.asin = self.single_element(root, "asin")
        album.duration = int(self.single_element(root, "duration")) 
        album.release = self.single_element(root, "release")
        album.disc_count = int(self.single_element(root, "disc_count"))
        album.track_count = int(self.single_element(root, "track_count"))
        album.active = self.single_element(root, "active")
        album.note = self.single_element(root, "note")
        album.format = self.single_element(root, "format")
        album.genre = self.single_element(root, "genre")

        for temp in root.findall('artist'):
            artist = self.get_artist(temp)
            album.artist = artist

        for temp in root.findall('song'):
            album.songs.append(self.get_song(temp))

        return album

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
