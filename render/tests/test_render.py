import unittest
from settings import SOURCE_PATH as the_path
from render.Render import Render
from utils.io import get_all_dirs, get_all_site_paths, get_template_path

class RenderTestCase(unittest.TestCase):
    site_path = get_all_site_paths(the_path)[0]
    def test_render(self):
        self.assertEqual(isinstance(Render(get_template_path(self.site_path)), Render), True)


if __name__ == '__main__':
    unittest.main()
