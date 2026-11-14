"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_binary_digits_count.py', '20\n0', '3\n'),
 ('001_binary_digits_count.py', '15\n1', '4\n'),
 ('001_binary_digits_count.py', '10\n0', '2\n'),
 ('002_bit_at_position_1.py', '2', '1\n'),
 ('002_bit_at_position_1.py', '51', '1\n'),
 ('002_bit_at_position_1.py', '13', '0\n'),
 ('002_bit_at_position_1.py', '24', '0\n'),
 ('003_pth_bit.py', '2145\n5', '1\n'),
 ('003_pth_bit.py', '512\n0', '0\n'),
 ('003_pth_bit.py', '111\n8', '0\n'),
 ('003_pth_bit.py', '255\n7', '1\n'),
 ('004_bit_destroyer.py', '1313\n5', '1281\n'),
 ('004_bit_destroyer.py', '231\n2', '227\n'),
 ('004_bit_destroyer.py', '111\n6', '47\n'),
 ('004_bit_destroyer.py', '111\n4', '111\n'),
 ('005_odd_times.py', '1 2 3 2 3 1 3', '3\n'),
 ('005_odd_times.py', '5 7 2 7 5 2 5', '5\n'),
 ('006_tri_bit_switch.py', '1234\n7', '1874\n'),
 ('006_tri_bit_switch.py', '44444\n4', '44524\n')]


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
