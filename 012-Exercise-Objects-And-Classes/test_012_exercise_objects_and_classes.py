"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_article.py', '', 'new title - new content: new author\n'),
 ('002_catalogue.py',
  '',
  "['Chair', 'Carpet']\nItems in the Furniture catalogue:\nCarpet\nChair\nDesk\nMirror\nSofa\n"),
 ('003_class.py', '', 'The students in 11B: Peter, George, Amy. Average grade: 4.77\n'),
 ('004_inventory.py', '', 'not enough room in the inventory\n2\nItems: potion, sword.\nCapacity left: 0\n'),
 ('005_movie.py',
  '',
  'Movie name: Inception; Movie director: Me. Total watched movies: 2\n'
  'Movie name: The Matrix; Movie director: The Wachowskis. Total watched movies: 2\n'
  'Movie name: My Movie; Movie director: Shane Black. Total watched movies: 2\n'),
 ('006_storage.py', '', "['apple', 'banana', 'potato', 'tomato']\n"),
 ('007_town.py', '', 'Town: Sofia | Latitude: 42° 41\' 51.04" N | Longitude: 23° 19\' 26.94" E\n'),
 ('008_vehicle.py',
  '',
  'Sorry, not enough money\n'
  'Successfully bought a car. Change: 5000.00\n'
  'BMW car is owned by: George\n'
  'BMW car is on sale: 30000\n'),
 ('009_weapon.py',
  '',
  'shooting...\nshooting...\nshooting...\nshooting...\nshooting...\nno bullets left\nRemaining bullets: 0\n')]


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
