#
# Title: verifier.py
# Description: 
# 
import os
import sys

from model import Album, Artist, JsonParser, XmlParser
from reporter import Reporter

class Verifier:
    def mb_id_verify(self, album: Album) -> bool:
        retflag = True

        if album.mb_id is None:
            print("missing mb_id")
            retflag = False
        elif len(album.mb_id) < 36:
            print("missing mb_id")
            retflag = False

        return retflag
    
    def release_verify(self, album: Album) -> bool:
        retflag = True

        if album.release is None:
            print("missing release date")
            retflag = False
        elif len(album.release) < 4:
            print("missing release")
            retflag = False

        return retflag
    

    def track_verify(self, album: Album) -> bool:
        retflag = True

        legal_media = {"CD", "DIGITAL_MEDIA"}
        if album.format not in legal_media:
            print(f"illegal format: {album.format}")
            retflag = False

        if album.track_count != len(album.songs):
            print(album)
            print(album.track_count)
            print(album.songs)
            print(f"track count mismatch: {album.track_count} {len(album.songs)}")
            retflag = False

        for song in album.songs:
            target = f"choral_wave/{song.file_name}"

            if not os.path.exists(target):
                print(f"file not found: {target}")
                retflag = False

        return retflag

    def execute(self, file_name: str) -> int:
        print("verify: ", file_name)

        retcode = 0

        jp = JsonParser()
        album = jp.manifest_reader("choral_wave/manifest.json")
        if album is None:
            print("unable to parse chorale_wave/manifest.json")
            return -1
            
#        if not self.mb_id_verify(album):
#            print("mb_id verification failed")
#            return -1
        
#        if not self.release_verify(album):
#            print("release verification failed")
#            return -1
        
        if not self.track_verify(album):
            print("track verification failed")
            return -1

# https://musicbrainz.org/ws/2/release/83ff6988-2f79-40b9-82d5-437f2a5da5f3?inc=aliases%2Bartist-credits%2Blabels%2Bdiscids%2Brecordings&fmt=json

        return retcode

#
if __name__ == '__main__':
    retcode = -1

    if len(sys.argv) == 2:
        target = sys.argv[1]
        print(target)

        verifier = Verifier()
        retcode = verifier.execute(target)
    else:
        print("missing target filename")

    sys.exit(retcode)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
