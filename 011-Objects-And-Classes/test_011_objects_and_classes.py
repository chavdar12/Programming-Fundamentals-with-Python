"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_circle.py', '', '31.40\n78.50\n1.09\n'),
 ('002_comment.py', '', 'user1\nI like this book\n0\n'),
 ('003_email.py',
  'Peter John Hi\nGeorge Peter Hey\nStop\n0',
  'Peter says to John: Hi. Sent: True\nGeorge says to Peter: Hey. Sent: False\n'),
 ('004_party.py', 'Peter\nJohn\nEnd', 'Going: Peter, John\nTotal: 2\n'),
 ('005_zoo.py',
  'Great Zoo\n3\nmammal lion\nbird owl\nmammal bear\nmammal',
  'Mammals in Great Zoo: lion, bear\nTotal animals: 3\n')]


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
