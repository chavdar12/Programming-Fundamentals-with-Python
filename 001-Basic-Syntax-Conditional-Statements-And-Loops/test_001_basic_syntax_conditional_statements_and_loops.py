"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_largest_of_three_numbers.py', '2\n3\n1', '3\n'),
 ('002_number_between_1_and_100.py', '-5\n101\n50.5', 'The number 50.50 is between 1 and 100\n'),
 ('003_number_definer.py', '-0.5', 'small negative\n'),
 ('003_number_definer.py', '0', 'zero\n'),
 ('003_number_definer.py', '2000000', 'large positive\n'),
 ('004_patterns.py', '3', '*\n**\n***\n**\n*\n'),
 ('005_word_reverse.py', 'Hello', 'olleH\n')]


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
