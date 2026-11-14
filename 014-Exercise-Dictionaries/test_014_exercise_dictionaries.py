"""Runs every script in this lesson with the example input from the course PDF and checks its output."""
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

# (script, stdin, expected stdout)
CASES = [('001_a_miner_task.py', 'Gold\n155\nSilver\n10\nGold\n15\nstop', 'Gold -> 170\nSilver -> 10\n'),
 ('002_capitals.py', 'Bulgaria, Romania\nSofia, Bucharest', 'Bulgaria -> Sofia\nRomania -> Bucharest\n'),
 ('003_company_users.py',
  'SoftUni -> AA12345\nSoftUni -> BB12345\nMicrosoft -> CC12345\nSoftUni -> AA12345\nEnd',
  'Microsoft\n-- CC12345\nSoftUni\n-- AA12345\n-- BB12345\n'),
 ('004_count_chars_in_a_string.py', 'text', 't -> 2\ne -> 1\nx -> 1\n'),
 ('005_courses.py',
  'Programming Fundamentals : John Smith\n'
  'Programming Fundamentals : Linda Johnson\n'
  'JS Core : Will Wilson\n'
  'end',
  'Programming Fundamentals: 2\n-- John Smith\n-- Linda Johnson\nJS Core: 1\n-- Will Wilson\n'),
 ('006_dragon_army.py',
  '3\nRed Bazgargal 100 2500 25\nBlack Dargonax 200 3500 18\nRed Obsidion 220 2200 35',
  'Red::(160.00/2350.00/30.00)\n'
  '-Bazgargal -> damage: 100, health: 2500, armor: 25\n'
  '-Obsidion -> damage: 220, health: 2200, armor: 35\n'
  'Black::(200.00/3500.00/18.00)\n'
  '-Dargonax -> damage: 200, health: 3500, armor: 18\n'),
 ('007_force_book.py',
  'Lighter | Royal\n'
  'Darker | DCay\n'
  'Ivan Ivanov -> Lighter\n'
  'DCay -> Lighter\n'
  'FancyPlayer | Lighter\n'
  'Lumpawaroo',
  'Ivan Ivanov joins the Lighter side!\n'
  'DCay joins the Lighter side!\n'
  'Side: Lighter, Members: 3\n'
  '! DCay\n'
  '! Ivan Ivanov\n'
  '! Royal\n'
  'Side: FancyPlayer, Members: 1\n'
  '! Lighter\n'),
 ('008_judge.py',
  'Peter -> Algo -> 400\nGeorge -> Algo -> 300\nPeter -> DS -> 150\nno more time',
  'Algo: 2 participants\n'
  '1. Peter <::> 400\n'
  '2. George <::> 300\n'
  'DS: 1 participants\n'
  '1. Peter <::> 150\n'
  'Individual standings:\n'
  '1. Peter -> 550\n'
  '2. George -> 300\n'),
 ('009_legendary_farming.py',
  '3 Motes 5 stones 5 Shards\n6 leathers 255 fragments 7 Shards',
  'Valanyr obtained!\nfragments: 5\nshards: 5\nmotes: 3\nleathers: 6\nstones: 5\n'),
 ('010_moba_challenger.py',
  'Peter -> Adc -> 400\n'
  'George -> Jungle -> 300\n'
  'Simon -> Mid -> 200\n'
  'Simon -> Support -> 250\n'
  'Peter vs George\n'
  'Simon vs Peter\n'
  'Season end',
  'Simon: 450 skill\n'
  '- Support <::> 250\n'
  '- Mid <::> 200\n'
  'Peter: 400 skill\n'
  '- Adc <::> 400\n'
  'George: 300 skill\n'
  '- Jungle <::> 300\n'),
 ('010_moba_challenger.py',
  'A -> Mid -> 100\nA -> Top -> 500\nB -> Mid -> 200\nA vs B\nSeason end',
  'A: 600 skill\n- Top <::> 500\n- Mid <::> 100\n'),
 ('011_orders.py',
  'Beer 2.20 100\nIceTea 1.50 50\nNukaCola 3.30 80\nWater 1.00 500\nbuy',
  'Beer -> 220.00\nIceTea -> 75.00\nNukaCola -> 264.00\nWater -> 500.00\n'),
 ('012_ranking.py',
  'Part One Interview:success\n'
  'Js Fundamentals:fundExam\n'
  'end of contests\n'
  'Js Fundamentals=>fundExam=>Tracy=>350\n'
  'Part One Interview=>success=>Tracy=>250\n'
  'Part One Interview=>fail=>Bob=>400\n'
  'Js Fundamentals=>fundExam=>Bob=>100\n'
  'end of submissions',
  'Best candidate is Tracy with total 600 points.\n'
  'Ranking:\n'
  'Bob\n'
  '#  Js Fundamentals -> 100\n'
  'Tracy\n'
  '#  Js Fundamentals -> 350\n'
  '#  Part One Interview -> 250\n'),
 ('013_snow_white.py',
  'Pesho <:> Red <:> 2000\nTosho <:> Blue <:> 1000\nGosho <:> Red <:> 1000\nOnce upon a time',
  '(Red) Pesho <-> 2000\n(Red) Gosho <-> 1000\n(Blue) Tosho <-> 1000\n'),
 ('014_softuni_exam_results.py',
  'Peter-Java-84\nGeorge-C#-84\nGeorge-C#-94\nKatty-C#-90\nexam finished',
  'Results:\nGeorge | 94\nKatty | 90\nPeter | 84\nSubmissions:\nC# - 3\nJava - 1\n'),
 ('015_softuni_parking.py',
  '5\n'
  'register John CS1234JS\n'
  'register George JAVA123S\n'
  'register John AB4142CD\n'
  'unregister Andy\n'
  'unregister George',
  'John registered CS1234JS successfully\n'
  'George registered JAVA123S successfully\n'
  'ERROR: already registered with plate number CS1234JS\n'
  'ERROR: user Andy not found\n'
  'George unregistered successfully\n'
  'John => CS1234JS\n'),
 ('016_student_academy.py',
  '5\nJohn\n5.5\nJohn\n4.5\nAlice\n6\nAlice\n3\nGeorge\n5',
  'John -> 5.00\nGeorge -> 5.00\nAlice -> 4.50\n')]


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
