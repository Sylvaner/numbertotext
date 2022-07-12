"""
numbertotext : Convert number to text
Copyright (C) 2022 Sylvain DANGIN

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of  MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <http://www.gnu.org/licenses/>.
"""
simple_numbers = {
    '0': 'zéro',
    '1': 'un',
    '2': 'deux',
    '3': 'trois',
    '4': 'quatre',
    '5': 'cinq',
    '6': 'six',
    '7': 'sept',
    '8': 'huit',
    '9': 'neuf',
    '10': 'dix',
    '11': 'onze',
    '12': 'douze',
    '13': 'treize',
    '14': 'quatorze',
    '15': 'quinze',
    '16': 'seize',
    '17': 'dix-sept',
    '18': 'dix-huit',
    '19': 'dix-neuf',
    '71': 'soixante-et-onze', # Too much specials rules
    '80': 'quatre-vingts', # Exception with plural
    '100': 'cent',
    '00': '', # Ignore 00
    '000': '', # Ignore 000
    '1000': 'mille'
}

tens = {
    1: 'dix',
    2: 'vingt',
    3: 'trente',
    4: 'quarante',
    5: 'cinquante',
    6: 'soixante',
    7: 'soixante-dix',
    8: 'quatre-vingt',
    9: 'quatre-vingt-dix'
}

big_names = {
    3: 'mille',
    6: 'million',
    9: 'milliard',
    12: 'billion',
    15: 'billiard',
    18: 'trillion',
    21: 'trilliard',
    24: 'quatrillion'
}

def numbertotext(number):
    """Convert number to full text
    :param number: Number to convert
    :type number:  number
    :return:       Full text number
    :rtype:    str
    """
    return convert(str(number), '', '')

def convert(number, previous_text, trailing):
    """Main recursiv function for number to full text conversion
    :param number:         Current number to convert
    :param previous_text:  Previous text with left digits
    :param trailing:       Trailing digits (if call on part of the number)
    :type number:          str
    :type previous_text:   str
    :type trailing:        str
    """
    to_add = ''
    if number in simple_numbers:
        return concat_data(previous_text, simple_numbers[number])
    if len(number) == 2:
        return concat_data(previous_text, convert_tens(number))
    if only_zeros_left(number): # len > 2
        return previous_text
    if len(number) == 3:
        to_add = convert_hundreds(number, trailing)
        number = number[1:]
    else: # len(number) <= 12:
        [to_add, number] = big_numbers(number)
    previous_text = concat_data(previous_text, to_add)
    return convert(number, previous_text, '')

def big_numbers(number):
    """Convert big numbers (1000 to 999 999 999 999)
    :param number: Number to convert
    :param type:   str
    :return:       Converted number
    :rtype:        str
    """
    number_range = ((len(number) - 1) // 3) * 3
    number_part = len(number) - number_range
    to_add = convert(number[:number_part], '', number[number_part:])
    if to_add == '':
        return ['', number[number_part:]]
    range_name = big_names[number_range]
    # plural (mille has no plural)
    if to_add != simple_numbers['1'] and number_range > 3:
        range_name += 's'
    elif to_add == simple_numbers['1'] and number_range == 3:
        # No unit before mille
        return ['mille', number[number_part:]]
    return [to_add + '-' + range_name, number[number_part:]]

def convert_tens(number):
    """Convert number with two digits
    :param number: Number with three digits
    :type:         str
    :return:       Full text number
    :rtype:        str
    """
    if number in simple_numbers:
        return simple_numbers[number]

    ten_number = int(number[0])
    if ten_number == 0:
        return simple_numbers[number[1]]
    unit_number = int(number[1])
    ten_text = tens[ten_number]

    if unit_number == 0:
        return ten_text

    unit_text = simple_numbers[number[1]]
    if ten_number == 7 or ten_number == 9:
        # Special case for 7x and 9x (60 and 11 for 71)
        unit_text = simple_numbers[str(10 + unit_number)]
    elif ten_number >= 2 and ten_number <= 6 and unit_number == 1:
        # Special case for 21, 31, ..., 61, (30 and 1)
        unit_text = 'et-' + unit_text
    if ten_number == 7 or ten_number == 9:
        # Special case for 70 and 90 (60-10 => 70, 80-10 => 90)
        ten_text = tens[ten_number - 1]
    return ten_text + '-' + unit_text

def only_zeros_left(number):
    """Test if only zeros left in number
    :param number: Number to test
    :type number:  str
    :return:       True if number contains only zeros
    :rtype:        boolean
    """
    return '0' * len(number) == number

def convert_hundreds(number, trailing):
    """Convert number with three digits
    :param number:   Number with three digits
    :param trailing: Trailing digits
    :type number:    str
    :type trailing:  str
    :return:         Full text number
    :rtype:          str
    """
    result = ''
    if number[0] == '0':
        return ''
    elif number[0] == '1':
        result = simple_numbers['100']
    else:
        result = simple_numbers[number[0]] + '-cent'
    if only_zeros_left(trailing) and only_zeros_left(number[1:]):
        # Only plural if no trailing digits
        result += 's'
    return result

def concat_data(current, data_to_add):
    """Concat number with previous text
    """
    if current == '':
        return data_to_add
    elif data_to_add != '':
        return current + '-' + data_to_add
    else:
        return current
