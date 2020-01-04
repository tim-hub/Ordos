import hashlib
from os import path

from jinja2 import Environment, select_autoescape, Template, FileSystemLoader


class Render:
    def __init__(self, templates_dir: str):
        self._templates_dir = templates_dir
        self._env = Environment(
            autoescape=select_autoescape(
                enabled_extensions=('html', 'xml'),
                default_for_string=True,
            ),
            loader=FileSystemLoader(path.abspath(self._templates_dir))
        )

    def __hash__(self):
        return hash(self._env)

    def __eq__(self, other: any) -> bool:
        return hash(self) == hash(other)

    @property
    def content(self) -> Template:
        return self._env.get_template('content.html')

    @property
    def home(self):
        return self._env.get_template('home.html')

    @property
    def archive(self):
        '''
        a collections of all contents
        :return:
        '''
        return self._env.get_template('archive.html')

    @property
    def list(self):
        '''
        a collection of contents list only
        :return:
        '''
        return self._env.get_template('list.html')


    def get_content_html(self, data) -> str:
        return self.content.render({'data':data})


    def get_home_html(self, data)-> str:
        return self.home.render(data)


    def get_archive_html(self, data)-> str:
        return self.archive.render(data)


    def get_list_html(self, data) -> str:
        return self.list.render(data)
