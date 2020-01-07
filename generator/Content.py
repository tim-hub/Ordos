import hashlib

from markdown2 import markdown

from custom_typings import ContentType
from generator.utils import get_md_content, get_md_name, get_content_type, format_markdown
from settings import MARKDOWN_EXTRA


class Content:

    def __init__(self, md_path: str, site_url: str):
        self._site_url = site_url
        self._md_path = md_path

    def __hash__(self):
        return hash(self.content.encode('utf-8'))

    def __eq__(self, other: any) -> bool:
        return hash(self) == hash(other)

    @property
    def sha(self):
        return hashlib.sha256(self.content.encode('utf-8')).hexdigest()

    @property
    def path(self) -> str:
        return self._md_path

    @property
    def name(self) -> str:
        return self.metadata['title']

    @property
    def title(self) -> str:
        return self.name

    @property
    def created(self) -> str:
        return self.metadata['date']

    @property
    def url(self):
        return get_md_name(self._md_path) + '.html'

    @property
    def permanent_url(self):
        return self._site_url + self.url

    @property
    def content_type(self) -> ContentType:
        return get_content_type(self.path)

    @property
    def content(self) -> str:
        return get_md_content(self.path)

    @property
    def content_obj(self):
        return markdown(format_markdown(self.content), extras=MARKDOWN_EXTRA)

    @property
    def content_html(self):
        return self.content_obj

    @property
    def content_short(self):
        return self.content_obj.split('<!--more-->')[0]

    @property
    def metadata(self):
        return self.content_obj.metadata

    @property
    def amp(self):
        return True
