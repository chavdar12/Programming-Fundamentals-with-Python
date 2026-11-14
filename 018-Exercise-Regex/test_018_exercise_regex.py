"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_capture_the_numbers.py',
  "The300\nWhat is that?\nI think it's the 3rd movie.\nLets watch it at 22:45\n",
  '300 3 22 45\n'),
 ('002_find_emails.py',
  'Please contact us at: support@github.com. Or s.miller@mit.edu but not 1user@.com',
  'support@github.com\ns.miller@mit.edu\n'),
 ('003_extract_the_links.py',
  'Join WebStars now for free, at www.web-stars.com\n'
  'You can also support our partners:\n'
  'Internet - www.internet.com\n',
  'www.web-stars.com\nwww.internet.com\n'),
 ('004_find_occurrences_of_word_in_sentence.py',
  'How do you plan on achieving that? How? How can you even think of that?\nhow',
  '3\n'),
 ('004_find_occurrences_of_word_in_sentence.py', 'a+b a+b ab\na+b', '2\n'),
 ('005_find_variable_names_in_sentences.py',
  '__invalidVariable _evenMoreInvalidVariable_ _validVariable',
  'validVariable\n'),
 ('006_furniture.py',
  '>>Sofa<<312.23!3\n>>TV<<300!5\n>Invalid<<!5\nPurchase',
  'Bought furniture:\nSofa\nTV\nTotal money spend: 2436.69\n'),
 ('006_furniture.py', '>>Chair<<5!2\nPurchase', 'Bought furniture:\nChair\nTotal money spend: 10.00\n'),
 ('007_html_parser.py',
  '<html><head><title>News</title></head><body><p>Hello world</p></body></html>',
  'Title: News\nContent: Hello world\n'),
 ('008_nether_realms.py', 'M3ph-0.5s-0.5t0.0**', 'M3ph-0.5s-0.5t0.0** - 524 health, 8.00 damage\n'),
 ('008_nether_realms.py',
  'M3ph1st0**, Azazel',
  'Azazel - 615 health, 0.00 damage\nM3ph1st0** - 524 health, 16.00 damage\n'),
 ('009_race.py',
  'George, Peter, Bill, Tom\n'
  'G4e@55or%6g6!68e!!@\n'
  'R1@!3a$y4456@\n'
  'B5@i@#123ll\n'
  'G@e54o$r6ge#\n'
  '7P%et^#e5346r\n'
  'T$o553m&6\n'
  'end of race',
  '1st place: George\n2nd place: Peter\n3rd place: Tom\n'),
 ('010_softuni_bar_income.py',
  '%George%<Croissant>|2|10.3$\n%Peter%<Gum>|1|1.3$\n%Maria%<Cola>|1|2.4$\nend of shift',
  'George: Croissant - 20.60\nPeter: Gum - 1.30\nMaria: Cola - 2.40\nTotal income: 24.30\n'),
 ('010_softuni_bar_income.py', '%Ann%<Tea>|2|3$\nend of shift', 'Ann: Tea - 6.00\nTotal income: 6.00\n'),
 ('012_star_enigma.py',
  '2\nSTCDoghudd4=63333$D$0A53333\nEHfsytsnhf?8555&I&2C9555SR',
  'Attacked planets: 1\n-> Alderaa\nDestroyed planets: 1\n-> Cantonica\n')]


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
