"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_courses.py', '3\na\nb\nc', "['a', 'b', 'c']\n"),
 ('002_list_statistics.py', '3\n1\n-2\n0', '[1, 0]\n[-2]\nCount of positives: 2. Sum of negatives: -2\n'),
 ('003_numbers_filter.py', '4\n1\n-2\n3\n4\neven', '[-2, 4]\n'),
 ('003_numbers_filter.py', '3\n-3\n2\n5\nodd', '[-3, 5]\n'),
 ('004_search.py', '3\nab\nabc\nxyz\nab', "['abc', 'xyz', 'ab']\n['abc', 'ab']\n"),
 ('005_strange_zoo.py', 'tail\nbody\nhead', "['head', 'body', 'tail']\n")]


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
