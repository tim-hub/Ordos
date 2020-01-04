import unittest

from utils.io import get_all_markdowns, get_all_dirs, get_all_site_paths
from settings import SOURCE_PATH as the_path


class IOSTestCase(unittest.TestCase):
    def test_get_all_mds(self):
        r = get_all_markdowns(the_path)
        # should be more than 1
        self.assertLessEqual(1, len(r))
        for md in r:
            # all are markdowns
            self.assertRegex(md[len(md) - 3:], r'.[Mm][Dd]')
            with open(md, 'r') as file:
                self.assertNotEqual(file.read().find('---'), -1, md)

    def test_get_dirs(self):
        dirs = get_all_dirs(the_path)
        self.assertEqual(dirs, ['tim-hub.github.io'])
        sites = get_all_site_paths(the_path)
        self.assertEqual(sites, ['source_sample/tim-hub.github.io'])


if __name__ == '__main__':
    unittest.main()
