import hashlib

from markdown2 import markdown

from custom_typings import ContentType, ContentName
from generator.utils import get_md_content, get_md_name, get_content_type, format_markdown
from settings import MARKDOWN_EXTRA


class HtmlContent:

    def __init__(self, md_path: str):
        self._md_path = md_path

    def __hash__(self):
        return hashlib.sha256(self.content).hexdigest()

    def __eq__(self, other: any) -> bool:
        return hash(self) == hash(other)

    @property
    def path(self) -> str:
        return self._md_path

    @property
    def name(self) -> ContentName:
        return get_md_name(self.path)

    @property
    def content_type(self) -> ContentType:
        return get_content_type(self.path)

    @property
    def content(self) -> str:
        return get_md_content(self.path)

    @property
    def content_html(self):
        return markdown(format_markdown(self.content), extras=MARKDOWN_EXTRA)

    @property
    def metadata(self):
        return self.content_html.metadata
