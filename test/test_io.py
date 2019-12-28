import unittest

from generator.io import get_all_markdowns
from settings import THE_PATH as the_path


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


if __name__ == '__main__':
    unittest.main()
