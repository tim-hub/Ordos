import sys
import unittest
from os import chdir, path
import http.server
import socketserver
from settings import SITES, OUTPUT_PATH

if len(sys.argv) > 3:
    print('You have specified too many arguments')
    sys.exit()

if len(sys.argv) < 2:
    print('You need to specify command name')
    sys.exit()

command:str = sys.argv[1]


if command == 'generate':
    print('to run')

# force regenerate
# view locally

if command == 'serve':
    site:str = sys.argv[2]
    work_dir = path.join(path.dirname(__file__), OUTPUT_PATH + site)
    chdir(work_dir)

    PORT = 8888
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()