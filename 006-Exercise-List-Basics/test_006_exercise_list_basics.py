"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_big_numbers_lover.py', '4 9 2 7', '9742\n'),
 ('002_bread_factory.py',
  'rest-2|order-10|eggs-100|rest-10',
  'You gained 0 energy.\n'
  'Current energy: 100.\n'
  'You earned 10 coins.\n'
  'You bought eggs.\n'
  'You gained 10 energy.\n'
  'Current energy: 80.\n'
  'Day completed!\n'
  'Coins: 10\n'
  'Energy: 80\n'),
 ('002_bread_factory.py',
  'order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000',
  'You earned 10 coins.\n'
  'You earned 10 coins.\n'
  'You earned 10 coins.\n'
  'You bought flour.\n'
  'You had to rest!\n'
  'Closed! Cannot afford oven.\n'),
 ('003_car_race.py', '29 13 9 0 13 0 21 0 14 82 12', 'The winner is left with total time: 53.8\n'),
 ('004_easter_gifts.py',
  'Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes\n'
  'OutOfStock Eggs\n'
  'Required Spoon 2\n'
  'JustInCase ChocolateEgg\n'
  'No Money',
  'StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg\n'),
 ('005_faro_shuffle.py', 'a b c d e f g h\n5', "['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']\n"),
 ('005_faro_shuffle.py',
  'one two three four five six\n2',
  "['one', 'five', 'four', 'three', 'two', 'six']\n"),
 ('006_football_cards.py', 'A-1 A-5 A-10 B-2', 'Team A - 8; Team B - 10\n'),
 ('006_football_cards.py', 'A-1 A-2 A-3 A-4 A-5', 'Team A - 6; Team B - 11\nGame was terminated\n'),
 ('007_hello_france.py',
  'Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60\n120',
  '60.62 35.35 51.13\nProfit: 42.03\nHello, France!\n'),
 ('008_invert_values.py', '1 2 -3 -3 5', '[-1, -2, 3, 3, -5]\n'),
 ('009_josephus_permutation.py', '1 2 3 4 5 6 7\n3', '[3,6,2,7,5,1,4]\n'),
 ('010_messaging.py', '9992 562 8933\nThis is some message for you', 'hey\n'),
 ('011_multiples_list.py', '2\n5', '[2, 4, 6, 8, 10]\n'),
 ('012_number_beggars.py', '1, 2, 3, 4, 5\n2', '[9, 6]\n'),
 ('013_seize_the_fire.py',
  'High = 89#Low = 28#Medium = 77#Low = 23\n1250',
  'Cells:\n - 89\n - 28\n - 77\n - 23\nEffort: 54.25\nTotal Fire: 217\n'),
 ('014_survival_of_the_biggest.py', '10 9 8 7 6 5\n3', '10, 9, 8\n'),
 ('015_tic_tac_toe.py', '1 2 0\n0 2 1\n1 2 0', 'Second player won\n'),
 ('015_tic_tac_toe.py', '2 0 1\n0 1 0\n1 0 2', 'First player won\n'),
 ('015_tic_tac_toe.py', '1 2 1\n1 2 2\n2 1 1', 'Draw!\n'),
 ('016_zeros_to_back.py', '0, 1, 0, 3, 12', '[1, 3, 12, 0, 0]\n')]


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
