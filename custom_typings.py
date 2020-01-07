from enum import Enum
from typing import Tuple, Dict, NewType


class ContentType(Enum):
    COMMON = 'Common'  # default type
    HIDDEN = 'Hidden'  # content will not be generated to get_content_html
    LIST = 'List'  # content will be listed, will not be in homepage or sidebar, will still be in sitemap


ContentName = NewType('ContentName', str)
HtmlData = Dict[str, str]

NameHtmlTuple = Tuple[ContentName, ContentType, HtmlData]  # file name, type and get_content_html
