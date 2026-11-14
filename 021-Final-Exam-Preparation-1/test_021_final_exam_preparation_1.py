"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_the_imitation_game.py',
  'zzHe\nChangeAll|z|l\nInsert|2|o\nMove|3\nDecode',
  'The decrypted message is: Hello\n'),
 ('001_the_imitation_game.py',
  'owyouh\nMove|2\nMove|3\nInsert|3|are\nInsert|9|?\nDecode',
  'The decrypted message is: howareyou?\n'),
 ('002_destination_mapper.py',
  '=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=',
  'Destinations: Hawai, Cyprus\nTravel Points: 11\n'),
 ('002_destination_mapper.py', 'ThisIs some InvalidInput', 'Destinations: \nTravel Points: 0\n'),
 ('003_heroes_of_code_and_logic_vii.py',
  '2\n'
  'Solmyr 85 120\n'
  'Kyrre 99 50\n'
  'Heal - Solmyr - 10\n'
  'Recharge - Solmyr - 50\n'
  'TakeDamage - Kyrre - 66 - Orc\n'
  'CastSpell - Kyrre - 15 - ViewEarth\n'
  'End',
  'Solmyr healed for 10 HP!\n'
  'Solmyr recharged for 50 MP!\n'
  'Kyrre was hit for 66 HP by Orc and now has 33 HP left!\n'
  'Kyrre has successfully cast ViewEarth and now has 35 MP!\n'
  'Solmyr\n'
  '  HP: 95\n'
  '  MP: 170\n'
  'Kyrre\n'
  '  HP: 33\n'
  '  MP: 35\n'),
 ('003_heroes_of_code_and_logic_vii.py',
  '4\n'
  'Adela 90 150\n'
  'SirMullich 70 40\n'
  'Ivor 1 111\n'
  'Tyris 94 61\n'
  'Heal - SirMullich - 50\n'
  'Recharge - Adela - 100\n'
  'CastSpell - Tyris - 1000 - Fireball\n'
  'TakeDamage - Tyris - 99 - Fireball\n'
  'TakeDamage - Ivor - 3 - Mosquito\n'
  'End',
  'SirMullich healed for 30 HP!\n'
  'Adela recharged for 50 MP!\n'
  'Tyris does not have enough MP to cast Fireball!\n'
  'Tyris has been killed by Fireball!\n'
  'Ivor has been killed by Mosquito!\n'
  'Adela\n'
  '  HP: 90\n'
  '  MP: 200\n'
  'SirMullich\n'
  '  HP: 100\n'
  '  MP: 40\n')]


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
