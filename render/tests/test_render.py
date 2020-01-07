import unittest

from jinja2 import Template

from render.Render import Render
from settings import SOURCE_PATH as the_path, TEMPLATE_PATH, SITES


class RenderTestCase(unittest.TestCase):
    site_name = SITES['tim-hub.github.io']['name']
    site_path = the_path + SITES['tim-hub.github.io']['name']
    render = Render(TEMPLATE_PATH + SITES['tim-hub.github.io']['template'])

    def test_render(self):
        self.assertEqual(isinstance(self.render, Render), True)

    def test_template(self):
        self.assertEqual(isinstance(self.render.content, Template), True)
        self.assertEqual(isinstance(self.render.home, Template), True)
        self.assertEqual(isinstance(self.render.archive, Template), True)
        self.assertEqual(isinstance(self.render.list, Template), True)


if __name__ == '__main__':
    unittest.main()
