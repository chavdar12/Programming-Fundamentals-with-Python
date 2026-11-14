"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_calculate_rectangle_area.py', '3\n4', '12\n'),
 ('002_calculations.py', 'multiply\n5\n5', '25\n'),
 ('002_calculations.py', 'divide\n8\n2', '4\n'),
 ('003_grades.py', '3.33', 'Poor\n'),
 ('003_grades.py', '5.6', 'Excellent\n'),
 ('004_orders.py', 'water\n5', '5.00\n'),
 ('004_orders.py', 'coffee\n2', '3.00\n'),
 ('005_repeat_string.py', 'abc\n3', 'abcabcabc\n')]


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
