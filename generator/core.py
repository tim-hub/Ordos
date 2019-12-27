from functools import reduce

from markdown2 import markdown
from generator.md_io import get_all_markdowns
from settings import META_SEPARATOR

get_html = markdown


def format_meta(md_meta:str) -> str:
    """

    :param md_meta:
    :return:
    """
    def join_two_lines(a: str, b: str) -> str:
        if a.strip().find('tags:') and b.startswith('- '):
            return a + b[2:] + ', '
        else:
            return a + '\n' + b

    return reduce((join_two_lines), md_meta.split('\n'))

def format_markdown(md_content:str) -> str:
    """
    format metadata, multiline tags are not supported in markdown2
    :param md_content:
    :return:
    """
    tag_index = md_content.find('tags')
    if tag_index > -1:
        meta_end = md_content.find(META_SEPARATOR)
        r = format_meta(md_content[:meta_end])
        return r +  md_content[meta_end:]
    return md_content


def mds_to_htmls(the_path: str) -> None:
    def md_to_html(md:str) -> str:
        with open(md, 'r') as file:
            # https://github.com/trentm/python-markdown2/wiki/Extras
            content = file.read().strip()
            # print(format_markdown(content))
            return markdown(format_markdown(content), extras=['metadata', 'nofollow', 'fenced-code-blocks', 'code-friendly', 'footnotes'])

    return list(map(md_to_html, get_all_markdowns(the_path)))



