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

    def get_artist_name(self, artist: Artist) -> str:
        if artist.first_name == "EMPTY_STRING":
            return artist.last_name
        else:
            return f"{artist.last_name}, {artist.first_name}"

    def get_detail_filename(self, album: Album) -> str:
        # has the form artist_album.html
        artist_name = self.get_artist_name(album.artist)
        album_name = album.file_name.replace(".zip", "")

        candidate_list = list(f"{artist_name}_{album_name}")
        result_list = []

        dupe_flag = False
        for temp in candidate_list:
            if temp.isalnum():
                dupe_flag = False
                result_list.append(temp)
            else:
                if dupe_flag == False:
                    dupe_flag = True
                    result_list.append("_")

        result = "".join(result_list).lower()
        result = result + ".html"
  
        return result

    def write_detail(self, file_name: str, dd: dict):
        full_detail_name = os.path.join(self.doc_root, file_name)
        print(full_detail_name)

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
        detail_filename = self.get_detail_filename(album)

        dd = {}

        dd['artist'] = self.get_artist_name(album.artist)
        dd['release'] = album.release
        dd['title'] = album.title
        dd['songs'] = []

        for song in album.songs:
            dd['songs'].append(f"{song.title} ({self.get_artist_name(song.artist)})")

        self.write_detail(detail_filename, dd)

        return(album.title, dd['artist'], detail_filename)

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
#                print(temp1)
                # select each album
                for temp in temp1:
                    ndx_file.write(f"      <LI>{temp[1]} <A HREF='https://guycole.github.io/python3-lab/{temp[2]}'>{temp[0]}</A></LI>\n")

            ndx_file.write("    </OL>\n")
            ndx_file.write("  </BODY>\n")
            ndx_file.write("</HTML>\n")

    def processor(self, target: str) -> tuple:
        os.chdir("/tmp")

        jp = JsonParser()

        with zipfile.ZipFile(target) as choral_zip:
            with choral_zip.open('choral_wave/manifest.json') as raw_manifest:
                json_manifest = json.loads(raw_manifest.read())
                album = jp.manifest_parser(json_manifest)

                album_details = self.build_detail(album)
                return album_details

    def execute(self):
        candidates = []

        for root, dirs, files in os.walk(self.cw_root):
            for file in files:
                if file.endswith(".zip"):
                    candidates.append(os.path.join(root, file))

        ndx_dd = {}

        for candidate in candidates:
            details = self.processor(candidate)

            if details is not None:
                if details[1] not in ndx_dd:
                    ndx_dd[details[1]] = []

                    ndx_dd[details[1]].append(details)
 
        self.write_index(ndx_dd)
#
if __name__ == '__main__':
    cw_root = "/Users/gsc/documents/audio-s3sync/choral/wave"
    doc_root = "/Users/gsc/Documents/github/python3-lab/docs"

    pr = PageReport(cw_root, doc_root)
    pr.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
