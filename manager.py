import sys
import unittest

if len(sys.argv) > 2:
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
    import http.server
    import socketserver

    PORT = 8888
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()