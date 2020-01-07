import unittest

from generator.Site import Site
from settings import SOURCE_PATH as the_path
from utils.io import get_all_sites, get_all_files


class SiteTestCase(unittest.TestCase):
    sites = list(map(lambda s: Site(s['path'], s['name']), get_all_sites(the_path)))
    site = sites[0]
    source_path = site.source_path + '/root'
    output_path = site.output_dir

    def test_site_copy_files(self):
        self.site.save()
        self.site.copy_files()
        self.assertEqual(all(elem in get_all_files(self.output_path) for elem in get_all_files(self.source_path)), True,
                         'all files from root should be in output dir')

    def test_site_name(self):
        self.assertEqual(self.site.name, 'tim-hub.github.io')


if __name__ == '__main__':
    unittest.main()
