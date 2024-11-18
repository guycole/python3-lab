#
# Title: page_report.py
# Description: refresh github pages
# 
import json
import os
import sys
import zipfile

from model import Album, Artist, JsonParser, XmlParser
from reporter import Reporter

class PageReport():

    def __init__(self, cw_root: str, doc_root: str):
        self.cw_root = cw_root
        self.doc_root = doc_root

    def write_detail(self, file_name: str, dd: dict):
        full_detail_name = os.path.join(self.doc_root, file_name)

        with open(full_detail_name, 'wt') as detail_file:
            detail_file.write("<HTML>\n")
            detail_file.write("  <HEAD>\n")
            detail_file.write(f"    <TITLE>{dd['title']}</TITLE>\n")
            detail_file.write("  </HEAD>\n")
            detail_file.write("\n")
            detail_file.write("  <BODY BGCOLOR=white>\n")
            detail_file.write("    <UL>\n")
            detail_file.write(f"      <LI>{dd['artist']}</LI>\n")
            detail_file.write(f"      <LI>{dd['title']} ({dd['release']})</LI>\n")
            detail_file.write("      <OL>\n")

            for song in dd['songs']:
                detail_file.write(f"        <LI>{song}</LI>\n")

            detail_file.write("      </OL>\n")
            detail_file.write("    </UL>\n")
            detail_file.write("  </BODY>\n")
            detail_file.write("</HTML>\n")

    def build_detail(self, album: Album) -> tuple:
        artist_name = f"{album.artist.last_name}_{album.artist.first_name}"

        html_name = album.file_name.replace(".zip", ".html")

        detail_name = f"{artist_name}_{html_name}"
        detail_name = detail_name.lower()

        dd = {}
        dd['artist'] = f"{album.artist.last_name}, {album.artist.first_name}"
        dd['release'] = album.release
        dd['title'] = album.title
        dd['songs'] = []

        for song in album.songs:
            dd['songs'].append(f"{song.title} ({song.artist.last_name}, {song.artist.first_name})")

        self.write_detail(detail_name, dd)

        return(album.title, artist_name, detail_name)

    def write_index(self, ndx_dd: dict):
        sorted_ndx = dict(sorted(ndx_dd.items()))

        full_ndx_name = os.path.join(self.doc_root, "index.html")

        with open(full_ndx_name, 'wt') as ndx_file:
            ndx_file.write("<HTML>\n")
            ndx_file.write("  <HEAD>\n")
            ndx_file.write(f"    <TITLE>ChoralWave</TITLE>\n")
            ndx_file.write("  </HEAD>\n")
            ndx_file.write("\n")
            ndx_file.write("  <BODY BGCOLOR=white>\n")
            ndx_file.write("    <OL>\n")

            for element in sorted_ndx:
                # select by artist
                temp1 = sorted_ndx[element]
                # select each album
                for temp in temp1:
                    print(temp)

                    ndx_file.write(f"      <LI>{temp[1]}, {temp[0]}</LI>\n")

            ndx_file.write("    </OL>\n")
            ndx_file.write("  </BODY>\n")
            ndx_file.write("</HTML>\n")

    def processor(self, target: str):
        os.chdir("/tmp")

        jp = JsonParser()

        ndx_dd = {}

        print(target)
        with zipfile.ZipFile(target) as choral_zip:
            with choral_zip.open('choral_wave/manifest.json') as raw_manifest:
                json_manifest = json.loads(raw_manifest.read())
                album = jp.manifest_parser(json_manifest)

                album_details = self.build_detail(album)

                if album_details[1] not in ndx_dd:
                    ndx_dd[album_details[1]] = []

                ndx_dd[album_details[1]].append(album_details)
               
        self.write_index(ndx_dd)

    def execute(self):
        candidates = []

        for root, dirs, files in os.walk(self.cw_root):
            for file in files:
                if file.endswith(".zip"):
                    candidates.append(os.path.join(root, file))

        for candidate in candidates:
            self.processor(candidate)

#
if __name__ == '__main__':
    cw_root = "/Users/gsc/documents/audio-s3sync/choral/wave"
    doc_root = "/Users/gsc/Documents/github/python3-lab/docs"

    pr = PageReport(cw_root, doc_root)
    pr.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
