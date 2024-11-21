#
# Title: json_manifest.py
# Description: read from music brainz and create json manifest
# 
import os
import requests
import sys

from model import Album, Artist, JsonParser, XmlParser
from reporter import Reporter

class JsonManifest:

    def execute(self, target_mb_id: str, outzip: str) -> None:
        url = f"https://musicbrainz.org/ws/2/release/{target_mb_id}?inc=aliases%2Bartist-credits%2Blabels%2Bdiscids%2Brecordings&fmt=json"
        #print(url)
        raw = requests.get(url)
        if raw.status_code != 200:
            print(f"error: {raw.status_code}")
            return

        jp = JsonParser()
        album = jp.music_brainz_parser(outzip, raw.json())

        reporter = Reporter()
        temp = reporter.json_manifest(album, outzip)
        reporter.write_json_manifest(temp)

#
# argv[1] = outfile.zip
# argv[2] = musicbrainz id
#
if __name__ == '__main__':
    if len(sys.argv) == 3:
        outzip = sys.argv[1]       
        mb_id = sys.argv[2]
    else:
        print("use test default")
        outzip = "outfile.zip"
        mb_id = "c5331806-b3fe-42e0-9a55-9f1f99c57c28"
        mb_id = "36556a3b-c9a1-4392-9c1c-c567ea7e0aa9"

    jm = JsonManifest()
    jm.execute(mb_id, outzip)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
