#
# Title: model.py
# Description: 
# 
from bs4 import BeautifulSoup
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

    def __str__(self) -> str:
        return(f"Album: {self.title}, {self.file_name}")

class Artist:
    def __init__(self, last_name: str, first_name: str, mb_id: str):
        self.last_name = last_name
        self.first_name = first_name
        self.mb_id = mb_id

    def __str__(self) -> str:
       return f"Artist: {self.last_name}, {self.first_name}, {self.mb_id}"

class Parser:

    def single_element(self, root, key:str) -> str:
        for temp in root.findall(key):
            print(temp.tag)
            print(temp.text)
            return temp.text
        
        return None

    def reader(self, file_name: str) -> Album:
        print("reader")

        album = Album()

        dd = {}

        return album















































































































































































































































































































































        tree = et.parse(file_name)
        root = tree.getroot()
        print("lxlxxlxlx")
        print(type(root))

        xx = self.single_element(root, "file_name")
        print(xx)

        for temp in root.findall('title'):
            print(temp.tag)
            print(temp.text)

        for temp in root.findall('file_name'):
            print(temp.tag)
            print(temp.text)

        for temp in root.findall('version2'):
            print(temp.tag)
            print(temp.text)

#        for song in root.findall('song'):
#            duration = int(song.find('duration').text)
#            title = song.find('title').text
#            file_name = song.find('file_name').text
#            mb_id = song.find('mb_id').text
#            print(f"Title: {title}, File: {file_name}, mbid: {mb_id}")
#            print(duration)
#            print(type(duration))

#        with open(file_name, 'r') as f:
#            data = f.read()

#        bs_data = BeautifulSoup(data, "xml")
#        print(bs_data)
#        print(type(bs_data))

#        b_title = bs_data.find('child', {'song':'title'})
#        print(b_title)

#        b_unique = bs_data.find_all('title')
#        print(b_unique)

#    with open(file_name, "r") as stream:
#        try:
#            configuration = yaml.load(stream, Loader=SafeLoader)
#        except yaml.YAMLError as exc:
#            print(exc)

        return album

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
