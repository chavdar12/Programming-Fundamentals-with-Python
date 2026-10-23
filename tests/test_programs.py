import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

# script -> [(stdin, expected stdout), ...]; examples are mostly the official SoftUni ones
CASES = {
    '001-Basic-Syntax-Conditional-Statements-And-Loops/001.py': [
        ('2\n3\n1',
         '3\n'),
    ],
    '001-Basic-Syntax-Conditional-Statements-And-Loops/002.py': [
        ('-5\n101\n50.5',
         'The number 50.50 is between 1 and 100\n'),
    ],
    '001-Basic-Syntax-Conditional-Statements-And-Loops/003.py': [
        ('-0.5',
         'small negative\n'),
        ('0',
         'zero\n'),
        ('2000000',
         'large positive\n'),
    ],
    '001-Basic-Syntax-Conditional-Statements-And-Loops/004.py': [
        ('3',
         '*\n**\n***\n**\n*\n'),
    ],
    '001-Basic-Syntax-Conditional-Statements-And-Loops/005.py': [
        ('Hello',
         'olleH\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/001.py': [
        ('3',
         '1 sheep...2 sheep...3 sheep...'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/002.py': [
        ('1\n7',
         'Total cost: 37\nTotal spirit: 58\n'),
        ('3\n20',
         'Total cost: 558\nTotal spirit: 156\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/003.py': [
        ('Hello',
         'HHeelllloo'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/004.py': [
        ('17',
         'drink coke\n'),
        ('30',
         'drink whisky\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/005.py': [
        ('20.50\n1.25',
         'You made 7 cozonacs! Now you have 16 eggs and 2.45BGN left.\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/006.py': [
        ('pYtHoN',
         '[1, 3, 5]\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/007.py': [
        ('103',
         '310\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/008.py': [
        ('dog\nCAT\ngaming\nEND',
         '3\n'),
        ('CODING\nCAT\nDOG\nEND',
         'You need extra sleep\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/009.py': [
        ('Johnny',
         'Hello, my love!\n'),
        ('Peter',
         'Hello, Peter!\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/010.py': [
        ('86',
         'Not even for Wolf of Wall Street?!\n'),
        ('88',
         'Leo finally won the Oscar! Leo is happy\n'),
        ('90',
         'Leo got one already!\n'),
        ('50',
         'When will you give Leo an Oscar?\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/012.py': [
        ('2\n7',
         '6\n'),
        ('5\n5',
         '5\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/013.py': [
        ('abcde\naBcDe',
         'aBcde\naBcDe\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/014.py': [
        ('1987',
         '2013\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/015.py': [
        ('sunfishsandwater',
         '4\n'),
        ('ssandun',
         '1\n'),
    ],
    '002-Exercise-Basic-Syntax-Conditional-Statements-And-Loops/016.py': [
        ('sheep, sheep, wolf',
         'Please go away and stop eating my sheep\n'),
        ('sheep, wolf, sheep, sheep',
         'Oi! Sheep number 2! You are about to be eaten by a wolf!\n'),
    ],
    '003-Data-Types-And-Variables/001.py': [
        ('1',
         '1 centuries = 100 years = 36524 days = 876576 hours = 52594560 minutes\n'),
    ],
    '003-Data-Types-And-Variables/002.py': [
        ('John\nSmith\n->',
         'John->Smith\n'),
    ],
    '003-Data-Types-And-Variables/003.py': [
        ('1852',
         '1.85\n'),
    ],
    '003-Data-Types-And-Variables/004.py': [
        ('15',
         '1 -> False\n2 -> False\n3 -> False\n4 -> False\n5 -> True\n6 -> False\n7 -> True\n8 -> False\n9 -> False\n10 -> False\n11 -> False\n12 -> False\n13 -> False\n14 -> True\n15 -> False\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/001.py': [
        ('8\n(\n5 + 10\n)\n* 2 +\n(\n5\n)\n-12',
         'BALANCED\n'),
        ('2\n(\n5',
         'UNBALANCED\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/002.py': [
        ('2\n7\n3',
         '7\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/003.py': [
        ('abc\ndef\nghi',
         'abcdefghi\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/004.py': [
        ('3\n3\na\nb\nc',
         'def\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/005.py': [
        ('17\n3',
         '6\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/006.py': [
        ('5\n10',
         'Before:\na = 5\nb = 10\nAfter:\na = 10\nb = 5\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/007.py': [
        ('7\n2\n3\n4\n5',
         'Gladiator expenses: 16.00 aureus\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/008.py': [
        ('10\n20\n3\n3',
         '30\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/009.py': [
        ('3\n5',
         '3 companions received 90 coins each.\n'),
        ('15\n30',
         '19 companions received 102 coins each.\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/010.py': [
        ('7',
         'True\n'),
        ('8',
         'False\n'),
        ('1',
         'False\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/012.py': [
        ('60\n65',
         '< = > ? @ A\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/013.py': [
        ('2\n10\n2\n3\n5\n5\n5',
         '10 : 2 = 125 (3)\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/014.py': [
        ('3\nA\nb\nC',
         'The sum equals: 230\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/015.py': [
        ('2',
         'aaa\naab\naba\nabb\nbaa\nbab\nbba\nbbb\n'),
    ],
    '004-Exercise-Data-Types-And-Variables/016.py': [
        ('5\n20\n100\n100\n100\n20',
         'Insufficient capacity!\n240\n'),
    ],
    '005-Lists-Basics/001.py': [
        ('3\na\nb\nc',
         "['a', 'b', 'c']\n"),
    ],
    '005-Lists-Basics/002.py': [
        ('3\n1\n-2\n0',
         '[1, 0]\n[-2]\nCount of positives: 2. Sum of negatives: -2\n'),
    ],
    '005-Lists-Basics/003.py': [
        ('4\n1\n-2\n3\n4\neven',
         '[-2, 4]\n'),
        ('3\n-3\n2\n5\nodd',
         '[-3, 5]\n'),
    ],
    '005-Lists-Basics/004.py': [
        ('3\nab\nabc\nxyz\nab',
         "['abc', 'xyz', 'ab']\n['abc', 'ab']\n"),
    ],
    '005-Lists-Basics/005.py': [
        ('tail\nbody\nhead',
         "['head', 'body', 'tail']\n"),
    ],
    '006-Exercise-List-Basics/001.py': [
        ('4 9 2 7',
         '9742\n'),
    ],
    '006-Exercise-List-Basics/002.py': [
        ('rest-2|order-10|eggs-100|rest-10',
         'You gained 0 energy.\nCurrent energy: 100.\nYou earned 10 coins.\nYou bought eggs.\nYou gained 10 energy.\nCurrent energy: 80.\nDay completed!\nCoins: 10\nEnergy: 80\n'),
        ('order-10|order-10|order-10|flour-100|order-100|oven-100|order-1000',
         'You earned 10 coins.\nYou earned 10 coins.\nYou earned 10 coins.\nYou bought flour.\nYou had to rest!\nClosed! Cannot afford oven.\n'),
    ],
    '006-Exercise-List-Basics/003.py': [
        ('29 13 9 0 13 0 21 0 14 82 12',
         'The winner is left with total time: 53.8\n'),
    ],
    '006-Exercise-List-Basics/004.py': [
        ('Eggs StuffedAnimal Cozonac Sweets EasterBunny Eggs Clothes\nOutOfStock Eggs\nRequired Spoon 2\nJustInCase ChocolateEgg\nNo Money',
         'StuffedAnimal Spoon Sweets EasterBunny ChocolateEgg\n'),
    ],
    '006-Exercise-List-Basics/005.py': [
        ('a b c d e f g h\n5',
         "['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']\n"),
        ('one two three four five six\n2',
         "['one', 'five', 'four', 'three', 'two', 'six']\n"),
    ],
    '006-Exercise-List-Basics/006.py': [
        ('A-1 A-5 A-10 B-2',
         'Team A - 8; Team B - 10\n'),
        ('A-1 A-2 A-3 A-4 A-5',
         'Team A - 6; Team B - 11\nGame was terminated\n'),
    ],
    '006-Exercise-List-Basics/007.py': [
        ('Clothes->43.30|Shoes->25.25|Clothes->36.52|Clothes->20.90|Accessories->15.60\n120',
         '60.62 35.35 51.13\nProfit: 42.03\nHello, France!\n'),
    ],
    '006-Exercise-List-Basics/008.py': [
        ('1 2 -3 -3 5',
         '[-1, -2, 3, 3, -5]\n'),
    ],
    '006-Exercise-List-Basics/009.py': [
        ('1 2 3 4 5 6 7\n3',
         '[3,6,2,7,5,1,4]\n'),
    ],
    '006-Exercise-List-Basics/010.py': [
        ('9992 562 8933\nThis is some message for you',
         'hey\n'),
    ],
    '006-Exercise-List-Basics/011.py': [
        ('2\n5',
         '[2, 4, 6, 8, 10]\n'),
    ],
    '006-Exercise-List-Basics/012.py': [
        ('1, 2, 3, 4, 5\n2',
         '[9, 6]\n'),
    ],
    '006-Exercise-List-Basics/013.py': [
        ('High = 89#Low = 28#Medium = 77#Low = 23\n1250',
         'Cells:\n - 89\n - 28\n - 77\n - 23\nEffort: 54.25\nTotal Fire: 217\n'),
    ],
    '006-Exercise-List-Basics/014.py': [
        ('10 9 8 7 6 5\n3',
         '10, 9, 8\n'),
    ],
    '006-Exercise-List-Basics/015.py': [
        ('1 2 0\n0 2 1\n1 2 0',
         'Second player won\n'),
        ('2 0 1\n0 1 0\n1 0 2',
         'First player won\n'),
        ('1 2 1\n1 2 2\n2 1 1',
         'Draw!\n'),
    ],
    '006-Exercise-List-Basics/016.py': [
        ('0, 1, 0, 3, 12',
         '[1, 3, 12, 0, 0]\n'),
    ],
    '007-Functions/001.py': [
        ('3\n4',
         '12\n'),
    ],
    '007-Functions/002.py': [
        ('multiply\n5\n5',
         '25\n'),
        ('divide\n8\n2',
         '4\n'),
    ],
    '007-Functions/003.py': [
        ('3.33',
         'Poor\n'),
        ('5.6',
         'Excellent\n'),
    ],
    '007-Functions/004.py': [
        ('water\n5',
         '5.00\n'),
        ('coffee\n2',
         '3.00\n'),
    ],
    '007-Functions/005.py': [
        ('abc\n3',
         'abcabcabc\n'),
    ],
    '008-Exercise-Finctions/001.py': [
        ('23\n6\n10',
         '19\n'),
    ],
    '008-Exercise-Finctions/002.py': [
        ('2\n4\n-1\n2',
         '(-1, 2)\n'),
        ('3\n0\n2\n2',
         '(2, 2)\n'),
    ],
    '008-Exercise-Finctions/003.py': [
        ('a\nd',
         'b c\n'),
    ],
    '008-Exercise-Finctions/004.py': [
        ('int\n5',
         '10\n'),
        ('real\n2.5',
         '3.75\n'),
        ('string\nhi',
         '$hi$\n'),
    ],
    '008-Exercise-Finctions/005.py': [
        ('5\n2',
         '60.00\n'),
        ('0\n1',
         '1.00\n'),
    ],
    '008-Exercise-Finctions/006.py': [
        ('1 3 5 7 9\nexchange 1\nmax odd\nmin even\nfirst 2 odd\nlast 2 even\nexchange 3\nend',
         '2\nNo matches\n[5, 7]\n[]\n[3, 5, 7, 9, 1]\n'),
    ],
    '008-Exercise-Finctions/007.py': [
        ('30',
         '30% [%%%.......]\nStill loading...\n'),
        ('100',
         '100% Complete!\n[%%%%%%%%%%]\n'),
    ],
    '008-Exercise-Finctions/008.py': [
        ('2\n4\n-1\n2\n-5\n-5\n4\n-3',
         '(4, -3)(-5, -5)\n'),
        ('0\n0\n10\n0\n0\n0\n3\n4',
         '(0, 0)(10, 0)\n'),
    ],
    '008-Exercise-Finctions/009.py': [
        ('2\n3\n-1',
         'negative\n'),
        ('0\n-1\n2',
         'zero\n'),
        ('-2\n-3\n1',
         'positive\n'),
    ],
    '008-Exercise-Finctions/011.py': [
        ('1000435',
         'Odd sum = 9, Even sum = 4\n'),
    ],
    '008-Exercise-Finctions/012.py': [
        ('123, 323, 421, 121',
         'False\nTrue\nFalse\nTrue\n'),
    ],
    '008-Exercise-Finctions/013.py': [
        ('logIn',
         'Password must be between 6 and 10 characters\nPassword must have at least 2 digits\n'),
        ('MyPass123',
         'Password is valid\n'),
    ],
    '008-Exercise-Finctions/014.py': [
        ('6',
         'We have a perfect number!\n'),
        ('28',
         'We have a perfect number!\n'),
        ('5',
         "It's not so perfect.\n"),
    ],
    '008-Exercise-Finctions/015.py': [
        ('2\n5\n3',
         '2\n'),
    ],
    '008-Exercise-Finctions/016.py': [
        ('4',
         '1 1 2 4\n'),
        ('2',
         '1 1\n'),
    ],
    '009-Lists-Advanced/001.py': [
        ('3, 2, 1, 5, 8',
         '[1, 4]\n'),
    ],
    '009-Lists-Advanced/002.py': [
        ('Python',
         'Pythn\n'),
        ('AppLE',
         'ppL\n'),
    ],
    '009-Lists-Advanced/003.py': [
        ('wow father mom wow shirt stats\nwow',
         "['wow', 'mom', 'wow', 'stats']\nFound palindrome 2 times\n"),
    ],
    '009-Lists-Advanced/004.py': [
        ('1 2 3 4 2 1\n3',
         'Score: 2/6. Employees are not happy!\n'),
        ('1 1 1 5 5\n1',
         'Score: 2/5. Employees are not happy!\n'),
    ],
    '009-Lists-Advanced/005.py': [
        ('3-Buy groceries\n1-Wash car\n2-Go\nEnd',
         "['Wash car', 'Go', 'Buy groceries']\n"),
    ],
    '009-Lists-Advanced/006.py': [
        ('3\nadd 20\ninsert 0 15\nleave 0 5\nEnd',
         '[10, 0, 20]\n'),
    ],
    '010-Exercise-Lists-Advanced/001.py': [
        ('3\n1 0 0 1\n2 0 0 0\n0 3 0 1\n0-0 1-0 2-1 2-1 2-1 1-1 2-1',
         '2\n'),
    ],
    '010-Exercise-Lists-Advanced/002.py': [
        ('72olle 103doo 100ya',
         'Hello good day\n'),
    ],
    '010-Exercise-Lists-Advanced/003.py': [
        ('3\n. . #\n# . #\n. . .',
         '6\n'),
    ],
    '010-Exercise-Lists-Advanced/004.py': [
        ('10',
         '[2, 8]\n'),
        ('44',
         '[2, 8, 18, 16]\n'),
    ],
    '010-Exercise-Lists-Advanced/005.py': [
        ('8, 12, 38, 3, 17, 19, 25, 35, 50',
         "Group of 10's: [8, 3]\nGroup of 20's: [12, 17, 19]\nGroup of 30's: [25]\nGroup of 40's: [38, 35]\nGroup of 50's: [50]\n"),
    ],
    '010-Exercise-Lists-Advanced/006.py': [
        ('10@10@10@2\nJump 1\nJump 2\nLove!',
         "Place 3 has Valentine's day.\nCupid's last position was 3.\nCupid has failed 3 places.\n"),
        ('1@2\nJump 0\nLove!',
         "Place 0 has Valentine's day.\nCupid's last position was 0.\nCupid has failed 1 places.\n"),
    ],
    '010-Exercise-Lists-Advanced/007.py': [
        ('Iron, Wood, Sword\nCollect - Gold\nDrop - Wood\nCraft!',
         'Iron, Sword, Gold\n'),
        ('Iron, Sword\nCombine Items - Iron:Gold\nRenew - Iron\nCraft!',
         'Gold, Sword, Iron\n'),
    ],
    '010-Exercise-Lists-Advanced/008.py': [
        ('4\n######\n##  k#\n## ###\n## ###',
         'Kate got out in 5 moves\n'),
        ('3\n#####\n#k  #\n# ###',
         'Kate got out in 2 moves\n'),
        ('3\n###\n#k#\n###',
         'Kate cannot get out\n'),
    ],
    '010-Exercise-Lists-Advanced/009.py': [
        ('52 74 23 44 96 110\nShoot 5 10\nShoot 1 80\nStrike 2 1\nAdd 22 3\nEnd',
         'Invalid placement!\n52|100\n'),
    ],
    '010-Exercise-Lists-Advanced/010.py': [
        ('1.2.3',
         '1.2.4\n'),
        ('1.9.9',
         '2.0.0\n'),
    ],
    '010-Exercise-Lists-Advanced/011.py': [
        ('1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33',
         'Positive: 1, 0, 5, 3, 4, 12, 19\nNegative: -2, -100, -20, -33\nEven: -2, 0, 4, -100, -20, 12\nOdd: 1, 5, 3, 19, -33\n'),
    ],
    '010-Exercise-Lists-Advanced/012.py': [
        ('4\nXXXX 4\nXX 1\nXXXX 6\nXXX 3',
         '2 more chairs needed in room 3\n'),
        ('2\nXXX 2\nXX 1',
         'Game On, 2 free chairs left\n'),
    ],
    '010-Exercise-Lists-Advanced/013.py': [
        ('2, 3, 5, 15, 75\n10',
         '[10, 10, 10, 15, 55]\n'),
        ('2, 3, 5, 15, 75\n20',
         '[20, 20, 20, 20, 20]\n'),
    ],
    '010-Exercise-Lists-Advanced/014.py': [
        ('T2exs15ti23ng1_3cod1rs',
         'Testingodr\n'),
    ],
    '010-Exercise-Lists-Advanced/015.py': [
        ('arp, live, strong\nlively, alive, harp, sharp, armstrong',
         "['arp', 'live', 'strong']\n"),
    ],
    '010-Exercise-Lists-Advanced/016.py': [
        ('kiwi orange banana apple',
         'kiwi\norange\nbanana\n'),
    ],
    '011-Object-And-Classes/001.py': [
        ('',
         '31.40\n78.50\n1.09\n'),
    ],
    '011-Object-And-Classes/002.py': [
        ('',
         'user1\nI like this book\n0\n'),
    ],
    '011-Object-And-Classes/003.py': [
        ('Peter John Hi\nGeorge Peter Hey\nStop\n0',
         'Peter says to John: Hi. Sent: True\nGeorge says to Peter: Hey. Sent: False\n'),
    ],
    '011-Object-And-Classes/004.py': [
        ('Peter\nJohn\nEnd',
         'Going: Peter, John\nTotal: 2\n'),
    ],
    '011-Object-And-Classes/005.py': [
        ('Great Zoo\n3\nmammal lion\nbird owl\nmammal bear\nmammal',
         'Mammals in Great Zoo: lion, bear\nTotal animals: 3\n'),
    ],
    '012-Exercise-Object-And-Classes/001.py': [
        ('',
         'new title - new content: new author\n'),
    ],
    '012-Exercise-Object-And-Classes/002.py': [
        ('',
         "['Chair', 'Carpet']\nItems in the Furniture catalogue:\nCarpet\nChair\nDesk\nMirror\nSofa\n"),
    ],
    '012-Exercise-Object-And-Classes/003.py': [
        ('',
         'The students in 11B: Peter, George, Amy. Average grade: 4.77\n'),
    ],
    '012-Exercise-Object-And-Classes/004.py': [
        ('',
         'not enough room in the inventory\n2\nItems: potion, sword.\nCapacity left: 0\n'),
    ],
    '012-Exercise-Object-And-Classes/005.py': [
        ('',
         'Movie name: Inception; Movie director: Me. Total watched movies: 2\nMovie name: The Matrix; Movie director: The Wachowskis. Total watched movies: 2\nMovie name: My Movie; Movie director: Shane Black. Total watched movies: 2\n'),
    ],
    '012-Exercise-Object-And-Classes/006.py': [
        ('',
         "['apple', 'banana', 'potato', 'tomato']\n"),
    ],
    '012-Exercise-Object-And-Classes/007.py': [
        ('',
         'Town: Sofia | Latitude: 42° 41\' 51.04" N | Longitude: 23° 19\' 26.94" E\n'),
    ],
    '012-Exercise-Object-And-Classes/008.py': [
        ('',
         'Sorry, not enough money\nSuccessfully bought a car. Change: 5000.00\nBMW car is owned by: George\nBMW car is on sale: 30000\n'),
    ],
    '012-Exercise-Object-And-Classes/009.py': [
        ('',
         'shooting...\nshooting...\nshooting...\nshooting...\nshooting...\nno bullets left\nRemaining bullets: 0\n'),
    ],
    '013-Dictionaries/001.py': [
        ('a, b, c',
         "{'a': 97, 'b': 98, 'c': 99}\n"),
    ],
    '013-Dictionaries/002.py': [
        ('bread 10 butter 4',
         "{'bread': 10, 'butter': 4}\n"),
    ],
    '013-Dictionaries/003.py': [
        ('Java C# PHP PHP JAVA C java',
         'java c# c\n'),
    ],
    '013-Dictionaries/004.py': [
        ('bread: 4\ncheese: 2\nbread: 1\nstatistics',
         'Products in stock:\n- bread: 5\n- cheese: 2\nTotal Products: 2\nTotal Quantity: 7\n'),
    ],
    '013-Dictionaries/005.py': [
        ('cheese 10 bread 5\nsugar cheese',
         "Sorry, we don't have sugar\nWe have 10 of cheese left\n"),
    ],
    '013-Dictionaries/006.py': [
        ('Peter:123:programming_basics\nJohn:456:fundamentals\nprogramming_basics',
         'Peter - 123\n'),
    ],
    '013-Dictionaries/007.py': [
        ('3\ncute\nadorable\ncute\ncharming\nsmart\nclever',
         'cute - adorable, charming\nsmart - clever\n'),
    ],
    '014-Exercise-Dictionaries/001.py': [
        ('Gold\n155\nSilver\n10\nGold\n15\nstop',
         'Gold -> 170\nSilver -> 10\n'),
    ],
    '014-Exercise-Dictionaries/002.py': [
        ('Bulgaria, Romania\nSofia, Bucharest',
         'Bulgaria -> Sofia\nRomania -> Bucharest\n'),
    ],
    '014-Exercise-Dictionaries/003.py': [
        ('SoftUni -> AA12345\nSoftUni -> BB12345\nMicrosoft -> CC12345\nSoftUni -> AA12345\nEnd',
         'Microsoft\n-- CC12345\nSoftUni\n-- AA12345\n-- BB12345\n'),
    ],
    '014-Exercise-Dictionaries/004.py': [
        ('text',
         't -> 2\ne -> 1\nx -> 1\n'),
    ],
    '014-Exercise-Dictionaries/005.py': [
        ('Programming Fundamentals : John Smith\nProgramming Fundamentals : Linda Johnson\nJS Core : Will Wilson\nend',
         'Programming Fundamentals: 2\n-- John Smith\n-- Linda Johnson\nJS Core: 1\n-- Will Wilson\n'),
    ],
    '014-Exercise-Dictionaries/006.py': [
        ('3\nRed Bazgargal 100 2500 25\nBlack Dargonax 200 3500 18\nRed Obsidion 220 2200 35',
         'Red::(160.00/2350.00/30.00)\n-Bazgargal -> damage: 100, health: 2500, armor: 25\n-Obsidion -> damage: 220, health: 2200, armor: 35\nBlack::(200.00/3500.00/18.00)\n-Dargonax -> damage: 200, health: 3500, armor: 18\n'),
    ],
    '014-Exercise-Dictionaries/007.py': [
        ('Lighter | Royal\nDarker | DCay\nIvan Ivanov -> Lighter\nDCay -> Lighter\nFancyPlayer | Lighter\nLumpawaroo',
         'Ivan Ivanov joins the Lighter side!\nDCay joins the Lighter side!\nSide: Lighter, Members: 3\n! DCay\n! Ivan Ivanov\n! Royal\nSide: FancyPlayer, Members: 1\n! Lighter\n'),
    ],
    '014-Exercise-Dictionaries/008.py': [
        ('Peter -> Algo -> 400\nGeorge -> Algo -> 300\nPeter -> DS -> 150\nno more time',
         'Algo: 2 participants\n1. Peter <::> 400\n2. George <::> 300\nDS: 1 participants\n1. Peter <::> 150\nIndividual standings:\n1. Peter -> 550\n2. George -> 300\n'),
    ],
    '014-Exercise-Dictionaries/009.py': [
        ('3 Motes 5 stones 5 Shards\n6 leathers 255 fragments 7 Shards',
         'Valanyr obtained!\nfragments: 5\nshards: 5\nmotes: 3\nleathers: 6\nstones: 5\n'),
    ],
    '014-Exercise-Dictionaries/010.py': [
        ('Peter -> Adc -> 400\nGeorge -> Jungle -> 300\nSimon -> Mid -> 200\nSimon -> Support -> 250\nPeter vs George\nSimon vs Peter\nSeason end',
         'Simon: 450 skill\n- Support <::> 250\n- Mid <::> 200\nPeter: 400 skill\n- Adc <::> 400\nGeorge: 300 skill\n- Jungle <::> 300\n'),
        ('A -> Mid -> 100\nA -> Top -> 500\nB -> Mid -> 200\nA vs B\nSeason end',
         'A: 600 skill\n- Top <::> 500\n- Mid <::> 100\n'),
    ],
    '014-Exercise-Dictionaries/011.py': [
        ('Beer 2.20 100\nIceTea 1.50 50\nNukaCola 3.30 80\nWater 1.00 500\nbuy',
         'Beer -> 220.00\nIceTea -> 75.00\nNukaCola -> 264.00\nWater -> 500.00\n'),
    ],
    '014-Exercise-Dictionaries/012.py': [
        ('Part One Interview:success\nJs Fundamentals:fundExam\nend of contests\nJs Fundamentals=>fundExam=>Tracy=>350\nPart One Interview=>success=>Tracy=>250\nPart One Interview=>fail=>Bob=>400\nJs Fundamentals=>fundExam=>Bob=>100\nend of submissions',
         'Best candidate is Tracy with total 600 points.\nRanking:\nBob\n#  Js Fundamentals -> 100\nTracy\n#  Js Fundamentals -> 350\n#  Part One Interview -> 250\n'),
    ],
    '014-Exercise-Dictionaries/013.py': [
        ('Pesho <:> Red <:> 2000\nTosho <:> Blue <:> 1000\nGosho <:> Red <:> 1000\nOnce upon a time',
         '(Red) Pesho <-> 2000\n(Red) Gosho <-> 1000\n(Blue) Tosho <-> 1000\n'),
    ],
    '014-Exercise-Dictionaries/014.py': [
        ('Peter-Java-84\nGeorge-C#-84\nGeorge-C#-94\nKatty-C#-90\nexam finished',
         'Results:\nGeorge | 94\nKatty | 90\nPeter | 84\nSubmissions:\nC# - 3\nJava - 1\n'),
    ],
    '014-Exercise-Dictionaries/015.py': [
        ('5\nregister John CS1234JS\nregister George JAVA123S\nregister John AB4142CD\nunregister Andy\nunregister George',
         'John registered CS1234JS successfully\nGeorge registered JAVA123S successfully\nERROR: already registered with plate number CS1234JS\nERROR: user Andy not found\nGeorge unregistered successfully\nJohn => CS1234JS\n'),
    ],
    '014-Exercise-Dictionaries/016.py': [
        ('5\nJohn\n5.5\nJohn\n4.5\nAlice\n6\nAlice\n3\nGeorge\n5',
         'John -> 5.00\nGeorge -> 5.00\nAlice -> 4.50\n'),
    ],
    '015-Text-Processing/001.py': [
        ('Agd#53Dfg^&4F53',
         '53453\nAgdDfgF\n#^&\n'),
    ],
    '015-Text-Processing/002.py': [
        ('hi abc',
         'hihiabcabcabc\n'),
    ],
    '015-Text-Processing/003.py': [
        ('helLo\nSoftuni\nend',
         'helLo = oLleh\nSoftuni = inutfoS\n'),
    ],
    '015-Text-Processing/004.py': [
        ('ice\nkicegiciceeb',
         'kgb\n'),
    ],
    '015-Text-Processing/005.py': [
        ('Linux, Windows\nIt is not Linux, it is GNU/Linux. A Windows client',
         'It is not *****, it is GNU/*****. A ******* client\n'),
    ],
    '016-Exercise-Text-Processing/001.py': [
        ('.\n@\ndsg12gr5653feee5',
         '363\n'),
    ],
    '016-Exercise-Text-Processing/002.py': [
        ('Programming is cool!',
         'Surjudpplqj#lv#frro$\n'),
    ],
    '016-Exercise-Text-Processing/003.py': [
        ('Gosho Pesho',
         '53253\n'),
    ],
    '016-Exercise-Text-Processing/004.py': [
        ('There are so many emoticons nowadays :P :o :)',
         ':P\n:o\n:)\n'),
    ],
    '016-Exercise-Text-Processing/005.py': [
        ('C:\\Internal\\training-internal\\Template.pptx',
         'File name: Template\nFile extension: pptx\n'),
        ('C:\\a\\archive.tar.gz',
         'File name: archive.tar\nFile extension: gz\n'),
    ],
    '016-Exercise-Text-Processing/006.py': [
        ('2\nHere is a name @George| and an age #18*\n@Billy| #35*',
         'George is 18 years old.\nBilly is 35 years old.\n'),
    ],
    '016-Exercise-Text-Processing/007.py': [
        ('SoftUni Article\nSome content\nHello\nend of comments',
         '<h1>\nSoftUni Article\n</h1>\n<article>\nSome content\n</article>\n<div>\nHello\n</div>\n'),
    ],
    '016-Exercise-Text-Processing/008.py': [
        ('A12b s17G',
         '330.00\n'),
    ],
    '016-Exercise-Text-Processing/009.py': [
        ('.. | -- .- -.. . | -.-- --- ..-',
         'I MADE YOU\n'),
    ],
    '016-Exercise-Text-Processing/010.py': [
        ('aSd2&5s@1',
         'Unique symbols used: 5\nASDASD&&&&&S@\n'),
    ],
    '016-Exercise-Text-Processing/011.py': [
        ('aaaaabbbbbcdddeeeedssaa',
         'abcdedsa\n'),
    ],
    '016-Exercise-Text-Processing/012.py': [
        ('abv>1>1>2>2asdasd',
         'abv>>>>dasd\n'),
    ],
    '016-Exercise-Text-Processing/013.py': [
        ("1 2 1 3\nikegfp'jpne)bv=41P83X@\nujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA\nfind",
         'Found gold at 10N70W\nFound Silver at 32S43W\n'),
    ],
    '016-Exercise-Text-Processing/014.py': [
        ('sh, too_long_username_hey, jeff, john45, ab-cd, jeff$',
         'jeff\njohn45\nab-cd\n'),
    ],
    '016-Exercise-Text-Processing/015.py': [
        ('Cash$$$$$$Ca$$$$$$sh',
         'ticket "Cash$$$$$$Ca$$$$$$sh" - 6$\n'),
        ('$$$$$$$$$$$$$$$$$$$$, aabb  , th@@@@@@eemo@@@@@@ey',
         'ticket "$$$$$$$$$$$$$$$$$$$$" - 10$ Jackpot!\ninvalid ticket\nticket "th@@@@@@eemo@@@@@@ey" - 6@\n'),
        ('@@@@@@a@@@@@@@@@b@@@',
         'ticket "@@@@@@a@@@@@@@@@b@@@" - 6@\n'),
    ],
    '017-Regex/001.py': [
        ('13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016',
         'Day: 13, Month: Jul, Year: 1928\nDay: 10, Month: Nov, Year: 1934\nDay: 25, Month: Dec, Year: 1937\n'),
    ],
    '017-Regex/002.py': [
        ('Ivan Ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Test Testov, Ivan\tIvanov',
         'Ivan Ivanov Test Testov\n'),
    ],
    '017-Regex/003.py': [
        ('1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5',
         '1 -1 123 -123 123.456 -123.456\n'),
    ],
    '017-Regex/004.py': [
        ('+359 2 222 2222,359-2-222-2222, +359/2/222/2222, +359-2 222 2222 +359 2-222-2222, +359-2-222-222, +359-2-222-22222 +359-2-222-2222',
         '+359 2 222 2222, +359-2-222-2222\n'),
    ],
    '018-Exercise-Regex/001.py': [
        ("The300\nWhat is that?\nI think it's the 3rd movie.\nLets watch it at 22:45\n",
         '300 3 22 45\n'),
    ],
    '018-Exercise-Regex/002.py': [
        ('Please contact us at: support@github.com. Or s.miller@mit.edu but not 1user@.com',
         'support@github.com\ns.miller@mit.edu\n'),
    ],
    '018-Exercise-Regex/003.py': [
        ('Join WebStars now for free, at www.web-stars.com\nYou can also support our partners:\nInternet - www.internet.com\n',
         'www.web-stars.com\nwww.internet.com\n'),
    ],
    '018-Exercise-Regex/004.py': [
        ('How do you plan on achieving that? How? How can you even think of that?\nhow',
         '3\n'),
        ('a+b a+b ab\na+b',
         '2\n'),
    ],
    '018-Exercise-Regex/005.py': [
        ('__invalidVariable _evenMoreInvalidVariable_ _validVariable',
         'validVariable\n'),
    ],
    '018-Exercise-Regex/006.py': [
        ('>>Sofa<<312.23!3\n>>TV<<300!5\n>Invalid<<!5\nPurchase',
         'Bought furniture:\nSofa\nTV\nTotal money spend: 2436.69\n'),
        ('>>Chair<<5!2\nPurchase',
         'Bought furniture:\nChair\nTotal money spend: 10.00\n'),
    ],
    '018-Exercise-Regex/007.py': [
        ('<html><head><title>News</title></head><body><p>Hello world</p></body></html>',
         'Title: News\nContent: Hello world\n'),
    ],
    '018-Exercise-Regex/008.py': [
        ('M3ph-0.5s-0.5t0.0**',
         'M3ph-0.5s-0.5t0.0** - 524 health, 8.00 damage\n'),
        ('M3ph1st0**, Azazel',
         'Azazel - 615 health, 0.00 damage\nM3ph1st0** - 524 health, 16.00 damage\n'),
    ],
    '018-Exercise-Regex/009.py': [
        ('George, Peter, Bill, Tom\nG4e@55or%6g6!68e!!@\nR1@!3a$y4456@\nB5@i@#123ll\nG@e54o$r6ge#\n7P%et^#e5346r\nT$o553m&6\nend of race',
         '1st place: George\n2nd place: Peter\n3rd place: Tom\n'),
    ],
    '018-Exercise-Regex/010.py': [
        ('%George%<Croissant>|2|10.3$\n%Peter%<Gum>|1|1.3$\n%Maria%<Cola>|1|2.4$\nend of shift',
         'George: Croissant - 20.60\nPeter: Gum - 1.30\nMaria: Cola - 2.40\nTotal income: 24.30\n'),
        ('%Ann%<Tea>|2|3$\nend of shift',
         'Ann: Tea - 6.00\nTotal income: 6.00\n'),
    ],
    '018-Exercise-Regex/012.py': [
        ('2\nSTCDoghudd4=63333$D$0A53333\nEHfsytsnhf?8555&I&2C9555SR',
         'Attacked planets: 1\n-> Alderaa\nDestroyed planets: 1\n-> Cantonica\n'),
    ],
}


def test_every_program_has_a_case():
    scripts = {p.relative_to(ROOT).as_posix() for p in ROOT.glob("0*/*.py")}
    assert scripts == set(CASES)


@pytest.mark.parametrize(
    "script, stdin, expected",
    [(script, stdin, expected) for script, cases in CASES.items() for stdin, expected in cases],
)
def test_program_output(script, stdin, expected):
    result = subprocess.run(
        [sys.executable, script], input=stdin + "\n", capture_output=True, text=True, timeout=10, cwd=ROOT
    )
    assert result.stderr == ""
    assert result.stdout == expected
