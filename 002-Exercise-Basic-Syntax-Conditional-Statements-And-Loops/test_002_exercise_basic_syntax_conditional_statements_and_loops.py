"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_can_t_sleep_count_sheep.py', '3', '1 sheep...2 sheep...3 sheep...'),
 ('002_maximum_multiple.py', '1\n7', 'Total cost: 37\nTotal spirit: 58\n'),
 ('002_maximum_multiple.py', '3\n20', 'Total cost: 558\nTotal spirit: 156\n'),
 ('003_double_char.py', 'Hello', 'HHeelllloo'),
 ('004_drink_something.py', '17', 'drink coke\n'),
 ('004_drink_something.py', '30', 'drink whisky\n'),
 ('005_easter_bread.py', '20.50\n1.25', 'You made 7 cozonacs! Now you have 16 eggs and 2.45BGN left.\n'),
 ('006_find_the_capitals.py', 'pYtHoN', '[1, 3, 5]\n'),
 ('007_find_the_largest.py', '103', '310\n'),
 ('008_how_much_coffee_do_you_need.py', 'dog\nCAT\ngaming\nEND', '3\n'),
 ('008_how_much_coffee_do_you_need.py', 'CODING\nCAT\nDOG\nEND', 'You need extra sleep\n'),
 ('009_jenny_s_secret_message.py', 'Johnny', 'Hello, my love!\n'),
 ('009_jenny_s_secret_message.py', 'Peter', 'Hello, Peter!\n'),
 ('010_leonardo_dicaprio_oscars.py', '86', 'Not even for Wolf of Wall Street?!\n'),
 ('010_leonardo_dicaprio_oscars.py', '88', 'Leo finally won the Oscar! Leo is happy\n'),
 ('010_leonardo_dicaprio_oscars.py', '90', 'Leo got one already!\n'),
 ('010_leonardo_dicaprio_oscars.py', '50', 'When will you give Leo an Oscar?\n'),
 ('012_integer_operations.py', '2\n7', '6\n'),
 ('012_integer_operations.py', '5\n5', '5\n'),
 ('013_string_switch.py', 'abcde\naBcDe', 'aBcde\naBcDe\n'),
 ('014_next_happy_year.py', '1987', '2013\n'),
 ('015_sum_of_a_beach.py', 'sunfishsandwater', '4\n'),
 ('015_sum_of_a_beach.py', 'ssandun', '1\n'),
 ('016_wolf_in_sheep_s_clothing.py', 'sheep, sheep, wolf', 'Please go away and stop eating my sheep\n'),
 ('016_wolf_in_sheep_s_clothing.py',
  'sheep, wolf, sheep, sheep',
  'Oi! Sheep number 2! You are about to be eaten by a wolf!\n')]


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
