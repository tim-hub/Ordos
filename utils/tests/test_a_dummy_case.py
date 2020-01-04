import unittest


class Dummycase(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(True, True, 'always true')


if __name__ == '__main__':
    unittest.main()
