"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_add_and_subtract.py', '23\n6\n10', '19\n'),
 ('002_center_point.py', '2\n4\n-1\n2', '(-1, 2)\n'),
 ('002_center_point.py', '3\n0\n2\n2', '(2, 2)\n'),
 ('003_characters_in_range.py', 'a\nd', 'b c\n'),
 ('004_data_types.py', 'int\n5', '10\n'),
 ('004_data_types.py', 'real\n2.5', '3.75\n'),
 ('004_data_types.py', 'string\nhi', '$hi$\n'),
 ('005_factorial_division.py', '5\n2', '60.00\n'),
 ('005_factorial_division.py', '0\n1', '1.00\n'),
 ('006_array_manipulator.py',
  '1 3 5 7 9\nexchange 1\nmax odd\nmin even\nfirst 2 odd\nlast 2 even\nexchange 3\nend',
  '2\nNo matches\n[5, 7]\n[]\n[3, 5, 7, 9, 1]\n'),
 ('007_loading_bar.py', '30', '30% [%%%.......]\nStill loading...\n'),
 ('007_loading_bar.py', '100', '100% Complete!\n[%%%%%%%%%%]\n'),
 ('008_longer_line.py', '2\n4\n-1\n2\n-5\n-5\n4\n-3', '(4, -3)(-5, -5)\n'),
 ('008_longer_line.py', '0\n0\n10\n0\n0\n0\n3\n4', '(0, 0)(10, 0)\n'),
 ('009_multiplication_sign.py', '2\n3\n-1', 'negative\n'),
 ('009_multiplication_sign.py', '0\n-1\n2', 'zero\n'),
 ('009_multiplication_sign.py', '-2\n-3\n1', 'positive\n'),
 ('011_odd_and_even_sum.py', '1000435', 'Odd sum = 9, Even sum = 4\n'),
 ('012_palindrome_integers.py', '123, 323, 421, 121', 'False\nTrue\nFalse\nTrue\n'),
 ('013_password_validator.py',
  'logIn',
  'Password must be between 6 and 10 characters\nPassword must have at least 2 digits\n'),
 ('013_password_validator.py', 'MyPass123', 'Password is valid\n'),
 ('014_perfect_number.py', '6', 'We have a perfect number!\n'),
 ('014_perfect_number.py', '28', 'We have a perfect number!\n'),
 ('014_perfect_number.py', '5', "It's not so perfect.\n"),
 ('015_smallest_of_three_numbers.py', '2\n5\n3', '2\n'),
 ('016_tribonacci_sequence.py', '4', '1 1 2 4\n'),
 ('016_tribonacci_sequence.py', '2', '1 1\n')]


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
