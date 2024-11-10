#
# Title: verifier.py
# Description: 
# 
import os

from model import Album, Artist, JsonParser, XmlParser
from reporter import Reporter

class Verifier:
    def track_verify(self, album: Album) -> bool:
        retflag = True

        for song in album.songs:
            target = f"choral_wave/{song.file_name}"

            if not os.path.exists(target):
                print(f"file not found: {target}")
                retflag = False

        return retflag

    def execute(self, file_name: str) -> None:
        print("verify: ", file_name)

#        parser = XmlParser()
#        album = parser.reader(file_name)

        reporter = Reporter()
#        reporter.reporter(album)

        jj = JsonParser()
        album = jj.music_brainz_reader("bonjovi.json")
        reporter.reporter(album)
        datum = reporter.json_manifest(album, "enjoy_sandwich.zip")
        reporter.write_json_manifest(datum)

# https://musicbrainz.org/ws/2/release/83ff6988-2f79-40b9-82d5-437f2a5da5f3?inc=aliases%2Bartist-credits%2Blabels%2Bdiscids%2Brecordings&fmt=json

        return

if __name__ == '__main__':
    verifier = Verifier()
    result = verifier.execute("choral_wave/manifest.xml")
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
