"""numbertotext unit tests
"""
# pylint: disable=missing-function-docstring
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from numbertotext.numbertotext import numbertotext

class TestNumberToText(unittest.TestCase):
    """Test lists of numbers
    """
    def test_0(self):
        self.assertEqual(numbertotext(0), 'zéro')

    def test_1(self):
        self.assertEqual(numbertotext(1), 'un')

    def test_2(self):
        self.assertEqual(numbertotext(2), 'deux')

    def test_3(self):
        self.assertEqual(numbertotext(3), 'trois')

    def test_4(self):
        self.assertEqual(numbertotext(4), 'quatre')

    def test_5(self):
        self.assertEqual(numbertotext(5), 'cinq')

    def test_6(self):
        self.assertEqual(numbertotext(6), 'six')

    def test_7(self):
        self.assertEqual(numbertotext(7), 'sept')

    def test_8(self):
        self.assertEqual(numbertotext(8), 'huit')

    def test_9(self):
        self.assertEqual(numbertotext(9), 'neuf')

    def test_10(self):
        self.assertEqual(numbertotext(10), 'dix')

    def test_11(self):
        self.assertEqual(numbertotext(11), 'onze')

    def test_12(self):
        self.assertEqual(numbertotext(12), 'douze')

    def test_13(self):
        self.assertEqual(numbertotext(13), 'treize')

    def test_14(self):
        self.assertEqual(numbertotext(14), 'quatorze')

    def test_15(self):
        self.assertEqual(numbertotext(15), 'quinze')

    def test_16(self):
        self.assertEqual(numbertotext(16), 'seize')

    def test_17(self):
        self.assertEqual(numbertotext(17), 'dix-sept')

    def test_18(self):
        self.assertEqual(numbertotext(18), 'dix-huit')

    def test_19(self):
        self.assertEqual(numbertotext(19), 'dix-neuf')

    def test_20(self):
        self.assertEqual(numbertotext(20), 'vingt')

    def test_21(self):
        self.assertEqual(numbertotext(21), 'vingt-et-un')

    def test_30(self):
        self.assertEqual(numbertotext(30), 'trente')

    def test_31(self):
        self.assertEqual(numbertotext(31), 'trente-et-un')

    def test_32(self):
        self.assertEqual(numbertotext(32), 'trente-deux')

    def test_40(self):
        self.assertEqual(numbertotext(40), 'quarante')

    def test_41(self):
        self.assertEqual(numbertotext(41), 'quarante-et-un')

    def test_42(self):
        self.assertEqual(numbertotext(42), 'quarante-deux')

    def test_50(self):
        self.assertEqual(numbertotext(50), 'cinquante')

    def test_51(self):
        self.assertEqual(numbertotext(51), 'cinquante-et-un')

    def test_53(self):
        self.assertEqual(numbertotext(53), 'cinquante-trois')

    def test_60(self):
        self.assertEqual(numbertotext(60), 'soixante')

    def test_61(self):
        self.assertEqual(numbertotext(61), 'soixante-et-un')

    def test_64(self):
        self.assertEqual(numbertotext(64), 'soixante-quatre')

    def test_70(self):
        self.assertEqual(numbertotext(70), 'soixante-dix')

    def test_71(self):
        self.assertEqual(numbertotext(71), 'soixante-et-onze')

    def test_74(self):
        self.assertEqual(numbertotext(74), 'soixante-quatorze')

    def test_78(self):
        self.assertEqual(numbertotext(78), 'soixante-dix-huit')

    def test_80(self):
        self.assertEqual(numbertotext(80), 'quatre-vingts')

    def test_81(self):
        self.assertEqual(numbertotext(81), 'quatre-vingt-un')

    def test_86(self):
        self.assertEqual(numbertotext(86), 'quatre-vingt-six')

    def test_90(self):
        self.assertEqual(numbertotext(90), 'quatre-vingt-dix')

    def test_91(self):
        self.assertEqual(numbertotext(91), 'quatre-vingt-onze')

    def test_97(self):
        self.assertEqual(numbertotext(97), 'quatre-vingt-dix-sept')

    def test_100(self):
        self.assertEqual(numbertotext(100), 'cent')

    def test_101(self):
        self.assertEqual(numbertotext(101), 'cent-un')

    def test_124(self):
        self.assertEqual(numbertotext(124), 'cent-vingt-quatre')

    def test_500(self):
        self.assertEqual(numbertotext(500), 'cinq-cents')

    def test_799(self):
        self.assertEqual(numbertotext(799), 'sept-cent-quatre-vingt-dix-neuf')

    def test_1000(self):
        self.assertEqual(numbertotext(1000), 'mille')

    def test_1080(self):
        self.assertEqual(numbertotext(1080), 'mille-quatre-vingts')

    def test_1234(self):
        self.assertEqual(numbertotext(1234), 'mille-deux-cent-trente-quatre')

    def test_3000(self):
        self.assertEqual(numbertotext(3000), 'trois-mille')

    def test_6790(self):
        self.assertEqual(numbertotext(6790), 'six-mille-sept-cent-quatre-vingt-dix')

    def test_10000(self):
        self.assertEqual(numbertotext(10000), 'dix-mille')

    def test_12345(self):
        self.assertEqual(numbertotext(12345), 'douze-mille-trois-cent-quarante-cinq')

    def test_123456(self):
        self.assertEqual(numbertotext(123456),
                         'cent-vingt-trois-mille-quatre-cent-cinquante-six')

    def test_999900(self):
        self.assertEqual(numbertotext(999900),
                         'neuf-cent-quatre-vingt-dix-neuf-mille-neuf-cents')

    def test_1000000(self):
        self.assertEqual(numbertotext(1000000),
                         'un-million')

    def test_1234567(self):
        self.assertEqual(numbertotext(1234567),
                         'un-million-deux-cent-trente-quatre-mille-cinq-cent-' +
                         'soixante-sept')

    def test_40000075(self):
        self.assertEqual(numbertotext(40000075),
                         'quarante-millions-soixante-quinze')

    def test_400000000(self):
        self.assertEqual(numbertotext(400000000), 'quatre-cents-millions')

    def test_500000075(self):
        self.assertEqual(numbertotext(500000075),
                         'cinq-cent-millions-soixante-quinze')

    def test_1000000000(self):
        self.assertEqual(numbertotext(1000000000),
                         'un-milliard')

    def test_1234567890(self):
        self.assertEqual(numbertotext(1234567890),
                         'un-milliard-deux-cent-trente-quatre-millions-' +
                         'cinq-cent-soixante-sept-mille-huit-cent-quatre-vingt-dix')

    def test_4000000071(self):
        self.assertEqual(numbertotext(4000000071),
                         'quatre-milliards-soixante-et-onze')

    def test_1000000000000(self):
        self.assertEqual(numbertotext(1000000000000),
                         'un-billion')

    def test_4000000000000(self):
        self.assertEqual(numbertotext(4000000000000),
                         'quatre-billions')

    def test_1000000000000000(self):
        self.assertEqual(numbertotext(1000000000000000),
                         'un-billiard')

    def test_50000000000000000(self):
        self.assertEqual(numbertotext(50000000000000000),
                         'cinquante-billiards')

    def test_5000000000000000000(self):
        self.assertEqual(numbertotext(5000000000000000000),
                         'cinq-trillions')

    def test_123456789123456(self):
        self.assertEqual(numbertotext(123456789123456),
                         'cent-vingt-trois-billions-quatre-cent-cinquante-' +
                         'six-milliards-sept-cent-quatre-vingt-neuf-millions-' +
                         'cent-vingt-trois-mille-quatre-cent-cinquante-six')

    def test_maxint(self):
        self.assertEqual(numbertotext(sys.maxsize),
                         'neuf-trillions-deux-cent-vingt-trois-billiards-' +
                         'trois-cent-soixante-douze-billions-trente-six-milliards-' + 
                         'huit-cent-cinquante-quatre-millions-sept-cent-soixante-' + 
                         'quinze-mille-huit-cent-sept')

if __name__ == '__main__':
    unittest.main()
