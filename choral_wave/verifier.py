#
# Title: verifier.py
# Description: 
# 
import os

from model import Album, Artist, Parser

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

        parser = Parser()
        album = parser.reader(file_name)
        print(f"Album: {album.title}, {album.artist.last_name}, {album.release}")

        for song in album.songs:
            print(f"Song: {song.title}, {song.duration}, {song.file_name}") 

        self.track_verify(album)

        return

if __name__ == '__main__':
    verifier = Verifier()
    result = verifier.execute("choral_wave/manifest.xml")
    print(result)

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
