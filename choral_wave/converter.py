#
# Title: json_manifest.py
# Description: read from music brainz and create json manifest
# 
import os
import requests
import sys

from model import Album, Artist, JsonParser, XmlParser
from reporter import Reporter

class JsonConverter:

    def execute(self, target:str) -> None:
        parser = XmlParser()
        album = parser.reader("choral_wave/manifest.xml")
        print(f"{album.file_name} {album.mb_id}")

        url = f"https://musicbrainz.org/ws/2/release/{album.mb_id}?inc=aliases%2Bartist-credits%2Blabels%2Bdiscids%2Brecordings&fmt=json"
        # print(url)
        raw = requests.get(url)
        if raw.status_code != 200:
            print(f"error: {raw.status_code}")
            return

        jp = JsonParser()
        album = jp.music_brainz_parser(album.file_name, raw.json())

        reporter = Reporter()
        temp = reporter.json_manifest(album, album.file_name)
        reporter.write_json_manifest(temp)

#
if __name__ == '__main__':
    if len(sys.argv) == 2:
        target = sys.argv[1]
        JsonConverter().execute(target)
    else:
        print("missing target filename")

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
