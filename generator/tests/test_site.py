import unittest

from generator.Site import Site
from settings import SOURCE_PATH as the_path
from utils.io import get_all_sites


class SiteTestCase(unittest.TestCase):
    sites = list(map(lambda s: Site(s['path'], s['name']), get_all_sites(the_path)))
    site = sites[0]

    def test_sites(self):
        self.site.save()
        # serve(self.sites[0].output_dir)

    def test_site_name(self):
        self.assertEqual(self.site.name, 'tim-hub.github.io')




if __name__ == '__main__':
    unittest.main()
