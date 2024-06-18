#
# Title: http_server.py
# Description: demonstrate a python server
# curl -v http://localhost:8080
# curl -v -i -u admin -H "Content-Type: application/json" -d "{\"key\":\"aaa\", \"value\":\"bbb\"}" http://localhost:8080/demo/simple/
#
from sys import argv
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

class DemoServer(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

class Solution:
    def execute(self, port=8080) -> None:
        logging.basicConfig(level=logging.INFO)
        server_address = ('', port)
        httpd = HTTPServer(server_address, DemoServer)

        logging.info('Starting httpd...\n')

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

        httpd.server_close()
        logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    print("main")

    solution = Solution()   
    if len(argv) == 2:
         # specify port
         solution.execute(port=int(argv[1]))
    else:
        # use default port of 8080
        solution.execute()

#;;; Local Variables: ***
#;;; mode:python ***
#;;; End: ***
