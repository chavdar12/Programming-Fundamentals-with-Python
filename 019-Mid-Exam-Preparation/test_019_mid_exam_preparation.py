"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_computer_store.py',
  '1050\n200\n450\n2\n18.50\n16.86\nspecial',
  "Congratulations you've just bought a new computer!\n"
  'Price without taxes: 1737.36$\n'
  'Taxes: 347.47$\n'
  '-----------\n'
  'Total price: 1876.35$\n'),
 ('001_computer_store.py',
  '1023\n15\n-20\n-5.50\n450\n20\n17.66\n19.30\nregular',
  'Invalid price!\n'
  'Invalid price!\n'
  "Congratulations you've just bought a new computer!\n"
  'Price without taxes: 1544.96$\n'
  'Taxes: 308.99$\n'
  '-----------\n'
  'Total price: 1853.95$\n'),
 ('001_computer_store.py', 'regular', 'Invalid order!\n'),
 ('002_array_modifier.py',
  '23 -2 321 87 42 90 -123\nswap 1 3\nswap 3 6\nswap 1 0\nmultiply 1 2\nmultiply 2 1\ndecrease\nend',
  '86, 7382, 2369942, -124, 41, 89, -3\n'),
 ('002_array_modifier.py',
  '1 2 3 4\nswap 0 1\nswap 1 2\nswap 2 3\nmultiply 1 2\ndecrease\nend',
  '1, 11, 3, 0\n'),
 ('003_moving_target.py',
  '52 74 23 44 96 110\nShoot 5 10\nShoot 1 80\nStrike 2 1\nAdd 22 3\nEnd',
  'Invalid placement!\n52|100\n'),
 ('003_moving_target.py', '1 2 3 4 5\nStrike 0 1\nEnd', 'Strike missed!\n1|2|3|4|5\n')]


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
