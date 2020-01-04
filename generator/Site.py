import hashlib
from os import path, mkdir, chdir
from typing import Iterator

from generator.Content import Content
from generator.utils import get_all_markdowns
from render.Render import Render
from settings import OUTPUT_PATH
from utils.io import get_template_path


class Site:

    def __init__(self, site_path: str, name: str):
        '''

        :param site_path: the source
        :param name:
        '''
        self.name = name
        self.site_path = site_path
        self.output_dir = path.abspath(OUTPUT_PATH) + '/' + self.name + '/'
        self.markdowns = get_all_markdowns(site_path)
        self.template_path = get_template_path(self.site_path)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other: any) -> bool:
        return hash(self) == hash(other)

    @property
    def sha(self):
        return hashlib.sha256(self.name.encode('utf-8')).hexdigest()

    @property
    def render(self):
        return Render(self.template_path)

    @property
    def contents(self) -> Iterator[Content]:
        def get_html(md: str):
            content = Content(md)
            return content

        return map(lambda md: get_html(md), self.markdowns)

    def save(self):
        output_dir = self.output_dir
        if not path.exists(output_dir):
            mkdir(output_dir)

        for content in self.contents:
            with open(output_dir + content.url + '.html', 'w+') as file:
                file.write(self.render.get_content_html(data=content))

    @staticmethod
    def serve(port=8888):
        import http.server
        import socketserver
        Handler = http.server.SimpleHTTPRequestHandler
        chdir(self.output_dir)
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print("serving at port", port)
            httpd.serve_forever()
