"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_ascii_values.py', 'a, b, c', "{'a': 97, 'b': 98, 'c': 99}\n"),
 ('002_bakery.py', 'bread 10 butter 4', "{'bread': 10, 'butter': 4}\n"),
 ('003_odd_occurrences.py', 'Java C# PHP PHP JAVA C java', 'java c# c\n'),
 ('004_statistics.py',
  'bread: 4\ncheese: 2\nbread: 1\nstatistics',
  'Products in stock:\n- bread: 5\n- cheese: 2\nTotal Products: 2\nTotal Quantity: 7\n'),
 ('005_stock.py',
  'cheese 10 bread 5\nsugar cheese',
  "Sorry, we don't have sugar\nWe have 10 of cheese left\n"),
 ('006_students.py',
  'Peter:123:programming_basics\nJohn:456:fundamentals\nprogramming_basics',
  'Peter - 123\n'),
 ('007_word_synonyms.py',
  '3\ncute\nadorable\ncute\ncharming\nsmart\nclever',
  'cute - adorable, charming\nsmart - clever\n')]


def normalize(text):
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


class TestLesson(unittest.TestCase):
    def test_examples(self):
        for script, stdin, expected in CASES:
            with self.subTest(script=script, stdin=stdin):
                result = subprocess.run([sys.executable, str(HERE / script)], input=stdin + "\n",
                                        capture_output=True, text=True, timeout=10, cwd=HERE)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout, expected)

    def test_every_script_has_a_case(self):
        scripts = {p.name for p in HERE.glob("*.py") if not p.name.startswith("test_")}
        self.assertEqual(scripts - {c[0] for c in CASES}, set())


if __name__ == "__main__":
    unittest.main()
