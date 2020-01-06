import unittest

from generator.Site import Site
from settings import SOURCE_PATH as the_path
from utils.io import get_all_sites


class SiteTestCase(unittest.TestCase):
    sites = list(map(lambda s: Site(s['path'], s['name']), get_all_sites(the_path)))

    def test_sites(self):
        self.sites[0].save()
        # serve(self.sites[0].output_dir)
        return


if __name__ == '__main__':
    unittest.main()
