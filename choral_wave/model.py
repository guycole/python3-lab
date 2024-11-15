#
# Title: model.py
# Description: 
#
import json

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
        self.note = "No Note"
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
        self.artist = None
        self.title = title
        self.file_name = file_name
        self.mb_id = mb_id
        self.duration = duration

    def __str__(self) -> str:
        return f"Song: {self.title}, {self.duration}, {self.file_name}, {self.mb_id}"

class JsonParser:
    def music_brainz_artist(self, raw: str, mb_id: str) -> Artist:
        first_name = "EMPTY_STRING"
        last_name = "EMPTY_STRING"
        mb_id2 = "EMPTY_STRING"

        if raw is not None:
            tokens = raw.split(",")
            if len(tokens) > 1:
                last_name = tokens[0].strip()
                first_name = tokens[1].strip()
            else:
                last_name = raw.strip()

        if mb_id is not None:
            mb_id2 = mb_id

        return Artist(last_name, first_name, mb_id2)

    def music_brainz_parser(self, outzip: str, buffer: dict) -> Album:
        album = Album()

        album.version = "1.0"
        album.title = buffer["title"]
        album.file_name = outzip
        album.mb_id = buffer["id"]
        album.asin = buffer["asin"]
      #  album.duration = int(buffer["length"])
        album.release = buffer["date"]
        album.disc_count = len(buffer["media"])
        album.format = buffer["media"][0]["format"]
        album.genre = "Rock"

        artist_credit = buffer["artist-credit"]
        mb_id = artist_credit[0]["artist"]["id"]
        name = artist_credit[0]["artist"]["sort-name"]

        artist = Artist(name, "EMPTY_STRING", mb_id)
        album.artist = artist
    
        album.track_count = 0
        for media in buffer["media"]:
            for track in media["tracks"]:
                album.track_count += 1
                if album.format == "Digital Media":
                    file_name = f"track{album.track_count:02}.mp3"
                else:
                    file_name = f"track{album.track_count:02}.cdda.wav"

                song = Song(track['title'], file_name, track['id'], track['length'])

                id = track['artist-credit'][0]['artist']['id']
                sort_name = track['artist-credit'][0]['artist']['sort-name']
                song.artist = self.music_brainz_artist(sort_name, id) 
                album.songs.append(song)

        return album

    def music_brainz_reader(self, file_name: str) -> Album:
        album = Album()

        buffer = {}

        try:
            with open(file_name) as infile:
                buffer = json.load(infile)
                album = self.music_brainz_parser("fixme", buffer)
        except Exception as error:
            print(error)

        return album

class XmlParser:
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
