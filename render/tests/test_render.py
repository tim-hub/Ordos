import unittest

from jinja2 import Template

from render.Render import Render
from settings import SOURCE_PATH as the_path
from utils.io import get_all_site_paths, get_template_path


class RenderTestCase(unittest.TestCase):
    site_path = get_all_site_paths(the_path)[0]
    render = Render(get_template_path(site_path))

    def test_render(self):
        self.assertEqual(isinstance(self.render, Render), True)

    def test_template(self):
        self.assertEqual(isinstance(self.render.content, Template), True)
        self.assertEqual(isinstance(self.render.home, Template), True)
        self.assertEqual(isinstance(self.render.archive, Template), True)
        self.assertEqual(isinstance(self.render.list, Template), True)


if __name__ == '__main__':
    unittest.main()
