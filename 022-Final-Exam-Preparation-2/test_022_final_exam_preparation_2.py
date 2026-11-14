"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_world_tour.py',
  'Hawai::Cyprys-Greece\nAdd Stop:7:Rome\nRemove Stop:11:16\nSwitch:Hawai:Bulgaria\nTravel',
  'Hawai::RomeCyprys-Greece\n'
  'Hawai::Rome-Greece\n'
  'Bulgaria::Rome-Greece\n'
  'Ready for world tour! Planned stops: Bulgaria::Rome-Greece\n'),
 ('002_ad_astra.py',
  '#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|',
  'You have food to last you for: 2 days!\n'
  'Item: Bread, Best before: 19/03/21, Nutrition: 4000\n'
  'Item: Apples, Best before: 08/10/20, Nutrition: 200\n'
  'Item: Carrots, Best before: 06/08/20, Nutrition: 500\n'),
 ('002_ad_astra.py', 'Hello|#Invalid food#19/03/20#450|$5*(@', 'You have food to last you for: 0 days!\n'),
 ('003_pirates.py',
  'Tortuga||345000||1250\n'
  'Santo Domingo||240000||630\n'
  'Havana||410000||1100\n'
  'Sail\n'
  'Plunder=>Tortuga=>75000=>380\n'
  'Prosper=>Santo Domingo=>180\n'
  'End',
  'Tortuga plundered! 380 gold stolen, 75000 citizens killed.\n'
  '180 gold added to the city treasury. Santo Domingo now has 810 gold.\n'
  'Ahoy, Captain! There are 3 wealthy settlements to go to:\n'
  'Tortuga -> Population: 270000 citizens, Gold: 870 kg\n'
  'Santo Domingo -> Population: 240000 citizens, Gold: 810 kg\n'
  'Havana -> Population: 410000 citizens, Gold: 1100 kg\n'),
 ('003_pirates.py',
  'Nassau||95000||1000\n'
  'San Juan||930000||1250\n'
  'Campeche||270000||690\n'
  'Port Royal||320000||1000\n'
  'Port Royal||100000||2000\n'
  'Sail\n'
  'Prosper=>Port Royal=>-200\n'
  'Plunder=>Nassau=>94000=>750\n'
  'Plunder=>Nassau=>1000=>150\n'
  'Plunder=>Campeche=>150000=>690\n'
  'End',
  'Gold added cannot be a negative number!\n'
  'Nassau plundered! 750 gold stolen, 94000 citizens killed.\n'
  'Nassau plundered! 150 gold stolen, 1000 citizens killed.\n'
  'Nassau has been wiped off the map!\n'
  'Campeche plundered! 690 gold stolen, 150000 citizens killed.\n'
  'Campeche has been wiped off the map!\n'
  'Ahoy, Captain! There are 2 wealthy settlements to go to:\n'
  'San Juan -> Population: 930000 citizens, Gold: 1250 kg\n'
  'Port Royal -> Population: 420000 citizens, Gold: 3000 kg\n')]


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
