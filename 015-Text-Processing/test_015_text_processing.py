"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_digits_letters_and_other.py', 'Agd#53Dfg^&4F53', '53453\nAgdDfgF\n#^&\n'),
 ('002_repeat_strings.py', 'hi abc', 'hihiabcabcabc\n'),
 ('003_reverse_strings.py', 'helLo\nSoftuni\nend', 'helLo = oLleh\nSoftuni = inutfoS\n'),
 ('004_substring.py', 'ice\nkicegiciceeb', 'kgb\n'),
 ('005_text_filter.py',
  'Linux, Windows\nIt is not Linux, it is GNU/Linux. A Windows client',
  'It is not *****, it is GNU/*****. A ******* client\n')]


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
