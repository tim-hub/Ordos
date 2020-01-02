import unittest
from settings import TEMPLATES_DIR
from render.Render import Render

class RenderTestCase(unittest.TestCase):
    def test_render(self):
        Render(TEMPLATES_DIR)
        return


if __name__ == '__main__':
    unittest.main()
