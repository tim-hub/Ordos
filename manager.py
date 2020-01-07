import http.server
import socketserver
import sys
from os import chdir, path

from generator.Site import Site
from settings import OUTPUT_PATH, SOURCE_PATH

if len(sys.argv) > 3:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You need to specify command name')
    sys.exit()

command: str = sys.argv[1]

if command == 'generate':
    site_name: str = sys.argv[2]
    site = Site(path.join(SOURCE_PATH, site_name), site_name)
    site.generate()

# force regenerate
# view locally

if command == 'serve':
    site_name: str = sys.argv[2]
    work_dir = path.join(path.dirname(__file__), OUTPUT_PATH + site_name)
    chdir(work_dir)

    PORT = 8888
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()
