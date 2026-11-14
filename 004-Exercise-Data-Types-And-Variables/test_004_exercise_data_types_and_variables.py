"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_balanced_brackets.py', '8\n(\n5 + 10\n)\n* 2 +\n(\n5\n)\n-12', 'BALANCED\n'),
 ('001_balanced_brackets.py', '2\n(\n5', 'UNBALANCED\n'),
 ('002_integer_operations.py', '2\n7\n3', '7\n'),
 ('003_chars_to_string.py', 'abc\ndef\nghi', 'abcdefghi\n'),
 ('004_decrypting_messages.py', '3\n3\na\nb\nc', 'def\n'),
 ('005_elevator.py', '17\n3', '6\n'),
 ('006_exchange_integers.py', '5\n10', 'Before:\na = 5\nb = 10\nAfter:\na = 10\nb = 5\n'),
 ('007_gladiator_expenses.py', '7\n2\n3\n4\n5', 'Gladiator expenses: 16.00 aureus\n'),
 ('008_sum_of_numbers.py', '10\n20\n3\n3', '30\n'),
 ('009_party_profit.py', '3\n5', '3 companions received 90 coins each.\n'),
 ('009_party_profit.py', '15\n30', '19 companions received 102 coins each.\n'),
 ('010_prime_number_checker.py', '7', 'True\n'),
 ('010_prime_number_checker.py', '8', 'False\n'),
 ('010_prime_number_checker.py', '1', 'False\n'),
 ('012_print_part_of_the_ascii_table.py', '60\n65', '< = > ? @ A\n'),
 ('013_snowballs.py', '2\n10\n2\n3\n5\n5\n5', '10 : 2 = 125 (3)\n'),
 ('014_sum_of_chars.py', '3\nA\nb\nC', 'The sum equals: 230\n'),
 ('015_triples_of_latin_letters.py', '2', 'aaa\naab\naba\nabb\nbaa\nbab\nbba\nbbb\n'),
 ('016_water_overflow.py', '5\n20\n100\n100\n100\n20', 'Insufficient capacity!\n240\n')]


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
