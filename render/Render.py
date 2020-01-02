import hashlib
from os import path
from jinja2 import Environment, PackageLoader, select_autoescape, Template, FileSystemLoader


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
        print(self._env)
        content_template = self._env.get_template('content.html')
        # template = Template('Hello {{ name }}!')
        print(content_template.render(content=123))

    def __hash__(self):
        return hashlib.sha256(self._env).hexdigest()

    def __eq__(self, other: any) -> bool:
        return hash(self) == hash(other)
