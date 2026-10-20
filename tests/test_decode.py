# python3 -m unittest discover -s tests
import os, sys, unittest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'src'))
from decode import load_key, tokens, dec, norm

KEY = os.path.join(ROOT, 'data', 'key.tsv')
TR = os.path.join(ROOT, 'data', 'transcription_f102r.txt')

class TestDecode(unittest.TestCase):
    def setUp(self):
        self.k = load_key(KEY)
        self.lines = dict(tokens(TR))

    def test_line_count(self):
        self.assertEqual(len(self.lines), 30)
        self.assertEqual(sum(len(v) for v in self.lines.values()), 505)

    def test_key_values(self):
        self.assertEqual(self.k['G.67'], 're')
        self.assertEqual(self.k['B.42'], 'de')
        self.assertEqual(self.k['o.64'], 'no')
        self.assertEqual(self.k['19'], 'a')
        self.assertEqual(self.k['a++'], '')

    def test_known_lines(self):
        # 本文の読み（docs/READING.md）と一致すること
        self.assertEqual(''.join(dec(self.lines['102r.04'], self.k)), 'cartedasuogenerochevostra')
        self.assertEqual(''.join(dec(self.lines['102r.16'], self.k)), 'chevostraecelentiascrivesse')
        self.assertEqual(''.join(dec(self.lines['102r.30'], self.k)), 'dentialforsenonsariamalefare')

    def test_unknown_marked(self):
        out = ''.join(dec(self.lines['102r.20'], self.k))
        self.assertIn('[B.3]', out)

    def test_norm(self):
        self.assertEqual(norm('G.67?'), 'G.67')

if __name__ == '__main__':
    unittest.main()
