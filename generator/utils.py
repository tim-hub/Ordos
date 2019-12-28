import ntpath
from functools import reduce
from typing import List

from markdown2 import markdown

from custom_typings import NameHtmlTuple, ContentType, ContentName
from generator.io import get_all_markdowns
from settings import META_SEPARATOR, MARKDOWN_EXTRA


def format_meta(md_meta: str) -> str:
    def join_two_lines(a: str, b: str) -> str:
        if a.strip().find('tags:') and b.startswith('- '):
            return a + b[2:] + ', '
        else:
            return a + '\n' + b

    return reduce((join_two_lines), md_meta.split('\n'))


def format_markdown(md_content: str) -> str:
    """
    format metadata, multiline tags are not supported in markdown2
    :param md_content:
    :return:
    """
    tag_index = md_content.find('tags')
    if tag_index > -1:
        meta_end = md_content.find(META_SEPARATOR)
        r = format_meta(md_content[:meta_end])
        return r + md_content[meta_end:]
    return md_content


def get_content_type(md_path: str) -> ContentType:
    if md_path.find(ContentType.HIDDEN.value.lower()) > -1:
        return ContentType.HIDDEN
    elif md_path.find(ContentType.LIST.value.lower()) > -1:
        return ContentType.LIST
    else:
        return ContentType.COMMON


def get_md_name(md_path: str) -> ContentName:
    the_name: str = str(ntpath.basename(md_path))

    return ContentName(the_name[:len(the_name) - 3])


def get_md_content(md_path: str) -> str:
    with open(md_path, 'r') as file:
        return file.read().strip()


def mds_to_htmls(the_path: str) -> List[NameHtmlTuple]:
    def md_to_html(md_path: str) -> NameHtmlTuple:
        content = get_md_content(md_path)

        # https://github.com/trentm/python-markdown2/wiki/Extras
        return (get_md_name(md_path),
                get_content_type(md_path),
                markdown(format_markdown(content), extras=MARKDOWN_EXTRA)
                )

    return list(map(md_to_html, get_all_markdowns(the_path)))
