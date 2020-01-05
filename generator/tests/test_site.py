import unittest
from generator.Site import Site
from generator.utils import serve
from settings import SOURCE_PATH as the_path
from utils.io import get_all_site_paths

class SiteTestCase(unittest.TestCase):

    sites = list(map(lambda s: Site(s, 'tim-hub.github.io'), get_all_site_paths(the_path)))

    def test_sites(self):
        self.sites[0].save()
        # serve(self.sites[0].output_dir)
        return


if __name__ == '__main__':
    unittest.main()
