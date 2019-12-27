import unittest
from generator.core import mds_to_htmls, format_markdown, format_meta
from generator.md_io import get_all_markdowns
from settings import THE_PATH as the_path

class CoreTestCase(unittest.TestCase):
    def test_html(self):
        r = mds_to_htmls(the_path)
        print(r)

    def test_meta_format(self):
        test_content_one_line = '''a:b
tags: a
'''
        self.assertEqual(format_meta(test_content_one_line), test_content_one_line)
        test_content_multi_lines = '''a:b
tags: 
- a
- b'''
        self.assertNotEqual(format_meta(test_content_multi_lines), test_content_multi_lines)

    def test_md_format(self):
        with open(get_all_markdowns(the_path)[0], 'r') as file:
            r = format_markdown(file.read())
            self.assertEqual(r, '''title: Recommendation, a learning app
date: 2019-03-18 21:46:41
category: Application
tags: Certification, Python, C#, 
---

![python ipfs](https://ipfs.io/ipfs/QmNqvRnSUoLBMdn2DEgiGLUR1Lekbu7AVaWCaeYBQyuPyJ)
Solo learn is an app which is quite similar to Duolingo, the difference is that Solo Learn is for learning programming.

The course is not that difficult, not time consuming, but it is still good for preparing interview questions.

<!-- more -->

![C# ipfs](https://ipfs.io/ipfs/QmPpG8m8SPGwHrX8Vf4p5H3sn1jVA4MXNxGjsqVTjykdat)



Based on my experience in New Zealand, there were not really hard questions during inteviewing, so this app is quite good in this case.

These are 2 certifications I got recently, and I am in top 5 for a while in NZ region!!!!!

One interesting staff is `Challenging`, but your weapon is `programming language`.
''')


if __name__ == '__main__':
    unittest.main()
