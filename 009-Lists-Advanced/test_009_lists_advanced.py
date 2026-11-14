"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_even_numbers.py', '3, 2, 1, 5, 8', '[1, 4]\n'),
 ('002_no_vowels.py', 'Python', 'Pythn\n'),
 ('002_no_vowels.py', 'AppLE', 'ppL\n'),
 ('003_palindrome_strings.py',
  'wow father mom wow shirt stats\nwow',
  "['wow', 'mom', 'wow', 'stats']\nFound palindrome 2 times\n"),
 ('004_the_office.py', '1 2 3 4 2 1\n3', 'Score: 2/6. Employees are not happy!\n'),
 ('004_the_office.py', '1 1 1 5 5\n1', 'Score: 2/5. Employees are not happy!\n'),
 ('005_to_do_list.py', '3-Buy groceries\n1-Wash car\n2-Go\nEnd', "['Wash car', 'Go', 'Buy groceries']\n"),
 ('006_trains.py', '3\nadd 20\ninsert 0 15\nleave 0 5\nEnd', '[10, 0, 20]\n')]


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
