"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_centuries_to_minutes.py',
  '1',
  '1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes\n'),
 ('002_concat_names.py', 'John\nSmith\n->', 'John->Smith\n'),
 ('003_convert_meters_to_kilometers.py', '1852', '1.85\n'),
 ('004_special_numbers.py',
  '15',
  '1 -> False\n'
  '2 -> False\n'
  '3 -> False\n'
  '4 -> False\n'
  '5 -> True\n'
  '6 -> False\n'
  '7 -> True\n'
  '8 -> False\n'
  '9 -> False\n'
  '10 -> False\n'
  '11 -> False\n'
  '12 -> False\n'
  '13 -> False\n'
  '14 -> True\n'
  '15 -> False\n')]


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
