"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_ascii_sumator.py', '.\n@\ndsg12gr5653feee5', '363\n'),
 ('002_caesar_cipher.py', 'Programming is cool!', 'Surjudpplqj#lv#frro$\n'),
 ('003_character_multiplier.py', 'Gosho Pesho', '53253\n'),
 ('004_emoticon_finder.py', 'There are so many emoticons nowadays :P :o :)', ':P\n:o\n:)\n'),
 ('005_extract_file.py',
  'C:\\Internal\\training-internal\\Template.pptx',
  'File name: Template\nFile extension: pptx\n'),
 ('005_extract_file.py', 'C:\\a\\archive.tar.gz', 'File name: archive.tar\nFile extension: gz\n'),
 ('006_extract_person_information.py',
  '2\nHere is a name @George| and an age #18*\n@Billy| #35*',
  'George is 18 years old.\nBilly is 35 years old.\n'),
 ('007_html.py',
  'SoftUni Article\nSome content\nHello\nend of comments',
  '<h1>\nSoftUni Article\n</h1>\n<article>\nSome content\n</article>\n<div>\nHello\n</div>\n'),
 ('008_letters_change_numbers.py', 'A12b s17G', '330.00\n'),
 ('009_morse_code_translator.py', '.. | -- .- -.. . | -.-- --- ..-', 'I MADE YOU\n'),
 ('010_rage_quit.py', 'aSd2&5s@1', 'Unique symbols used: 5\nASDASD&&&&&S@\n'),
 ('011_replace_repeating_chars.py', 'aaaaabbbbbcdddeeeedssaa', 'abcdedsa\n'),
 ('012_string_explosion.py', 'abv>1>1>2>2asdasd', 'abv>>>>dasd\n'),
 ('013_treasure_finder.py',
  "1 2 1 3\nikegfp'jpne)bv=41P83X@\nujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA\nfind",
  'Found gold at 10N70W\nFound Silver at 32S43W\n'),
 ('014_valid_usernames.py', 'sh, too_long_username_hey, jeff, john45, ab-cd, jeff$', 'jeff\njohn45\nab-cd\n'),
 ('015_winning_ticket.py', 'Cash$$$$$$Ca$$$$$$sh', 'ticket "Cash$$$$$$Ca$$$$$$sh" - 6$\n'),
 ('015_winning_ticket.py',
  '$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey',
  'ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!\ninvalid ticket\nticket "th@@@@@@eemo@@@@@@ey" - 6@\n'),
 ('015_winning_ticket.py', '@@@@@@a@@@@@@@@@b@@@', 'ticket "@@@@@@a@@@@@@@@@b@@@" - 6@\n')]


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
