"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_battle_ships.py', '3\n1 0 0 1\n2 0 0 0\n0 3 0 1\n0-0 1-0 2-1 2-1 2-1 1-1 2-1', '2\n'),
 ('002_decipher_this.py', '72olle 103doo 100ya', 'Hello good day\n'),
 ('003_dots.py', '3\n. . #\n# . #\n. . .', '6\n'),
 ('004_electron_distribution.py', '10', '[2, 8]\n'),
 ('004_electron_distribution.py', '44', '[2, 8, 18, 16]\n'),
 ('005_group_of_10_s.py',
  '8, 12, 38, 3, 17, 19, 25, 35, 50',
  "Group of 10's: [8, 3]\n"
  "Group of 20's: [12, 17, 19]\n"
  "Group of 30's: [25]\n"
  "Group of 40's: [38, 35]\n"
  "Group of 50's: [50]\n"),
 ('006_heart_delivery.py',
  '10@10@10@2\nJump 1\nJump 2\nLove!',
  "Place 3 has Valentine's day.\nCupid's last position was 3.\nCupid has failed 3 places.\n"),
 ('006_heart_delivery.py',
  '1@2\nJump 0\nLove!',
  "Place 0 has Valentine's day.\nCupid's last position was 0.\nCupid has failed 1 places.\n"),
 ('007_inventory.py', 'Iron, Wood, Sword\nCollect - Gold\nDrop - Wood\nCraft!', 'Iron, Sword, Gold\n'),
 ('007_inventory.py', 'Iron, Sword\nCombine Items - Iron:Gold\nRenew - Iron\nCraft!', 'Gold, Sword, Iron\n'),
 ('008_kate_s_way_out.py', '4\n######\n##  k#\n## ###\n## ###', 'Kate got out in 5 moves\n'),
 ('008_kate_s_way_out.py', '3\n#####\n#k  #\n# ###', 'Kate got out in 2 moves\n'),
 ('008_kate_s_way_out.py', '3\n###\n#k#\n###', 'Kate cannot get out\n'),
 ('009_moving_target.py',
  '52 74 23 44 96 110\nShoot 5 10\nShoot 1 80\nStrike 2 1\nAdd 22 3\nEnd',
  'Invalid placement!\n52|100\n'),
 ('010_next_version.py', '1.2.3', '1.2.4\n'),
 ('010_next_version.py', '1.9.9', '2.0.0\n'),
 ('011_number_classification.py',
  '1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33',
  'Positive: 1, 0, 5, 3, 4, 12, 19\n'
  'Negative: -2, -100, -20, -33\n'
  'Even: -2, 0, 4, -100, -20, 12\n'
  'Odd: 1, 5, 3, 19, -33\n'),
 ('012_office_chairs.py', '4\nXXXX 4\nXX 1\nXXXX 6\nXXX 3', '2 more chairs needed in room 3\n'),
 ('012_office_chairs.py', '2\nXXX 2\nXX 1', 'Game On, 2 free chairs left\n'),
 ('013_social_distribution.py', '2, 3, 5, 15, 75\n10', '[10, 10, 10, 15, 55]\n'),
 ('013_social_distribution.py', '2, 3, 5, 15, 75\n20', '[20, 20, 20, 20, 20]\n'),
 ('014_take_skip_rope.py', 'T2exs15ti23ng1_3cod1rs', 'Testingodr\n'),
 ('015_which_are_in.py',
  'arp, live, strong\nlively, alive, harp, sharp, armstrong',
  "['arp', 'live', 'strong']\n"),
 ('016_word_filter.py', 'kiwi orange banana apple', 'kiwi\norange\nbanana\n')]


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
