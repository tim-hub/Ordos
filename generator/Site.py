import hashlib
from os import path, mkdir
from typing import Iterator

from generator.Content import Content
from generator.utils import get_all_markdowns
from render.Render import Render
from settings import OUTPUT_PATH, SITES, TEMPLATE_PATH


class Site:

    def __init__(self, source_path: str, name: str):
        '''

        :param source_path: the source
        :param name:
        '''
        self.name = name
        self.source_path = source_path
        if not path.exists(OUTPUT_PATH):
            mkdir(OUTPUT_PATH)
        self.output_dir = path.abspath(OUTPUT_PATH) + '/' + self.name + '/'
        self.markdowns = get_all_markdowns(source_path)
        self.template_path = TEMPLATE_PATH + SITES[self.name]['template']

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        return hash(self) == hash(other)

    @property
    def url(self) -> str:
        return SITES[self.name]['url']

    @property
    def sha(self) -> str:
        return hashlib.sha256(self.name.encode('utf-8')).hexdigest()

    @property
    def render(self):
        return Render(self.template_path)

    @property
    def contents(self) -> Iterator[Content]:
        def get_html(md: str):
            content = Content(md, self.url)
            return content

        return map(lambda md: get_html(md), self.markdowns)

    def contents_sorted(self):
        contents_sort = list(self.contents)
        contents_sort.sort(key=lambda c: c.created, reverse=True)
        return contents_sort

    def generate(self):
        self.copy_files()
        self.save()

    def copy_files(self):
        from distutils.dir_util import copy_tree
        copy_tree(self.source_path + '/root', self.output_dir)
        copy_tree(self.template_path + '/root', self.output_dir)

    def save(self):
        output_dir = self.output_dir
        if not path.exists(output_dir):
            mkdir(output_dir)

        for content in self.contents_sorted():
            with open(output_dir + content.url, 'w+') as file:
                file.write(self.render.get_content_html(data=content))

        with open(output_dir + 'index.html', 'w+') as file:
            file.write(self.render.get_home_html(
                data={
                    'contents': self.contents_sorted(),
                    'data': {
                        'metadata': {}
                    }
                }
            ))
