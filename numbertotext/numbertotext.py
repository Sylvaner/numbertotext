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

    Parameters
    ----------
    number : int
        Number to convert

    Returns
    -------
    str
        Text version of the number
    """
    return convert(str(number), '', '')

def convert(number, previous_text, trailing):
    """Main recursive function that convert number to full text conversion

    Parameters
    ----------
    number : str
        Number to convert (numeric format)
    previous_text : str
        Digits encoded buffer
    trailing : str
        Digits to encode after this number

    Returns
    -------
    str
        Text version of the number
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
    else:
        [to_add, number] = big_numbers(number)
    previous_text = concat_data(previous_text, to_add)
    return convert(number, previous_text, '')

def big_numbers(number):
    """Convert big numbers (1000 to 999 999 999 999)

    Parameters
    ----------
    number : str
        Number to convert

    Returns
    -------
    str
        Text version of the number
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

    Parameters
    ----------
    number : str
        2 digits number

    Returns
    -------
    str
        Text version of the number
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
    if ten_number in (7, 9):
        # Special case for 70 and 90 (60-10 => 70, 80-10 => 90)
        ten_text = tens[ten_number - 1]
        # Special case for 7x and 9x (60 and 11 for 71)
        unit_text = simple_numbers[str(10 + unit_number)]
    elif 2 <= ten_number <= 6 and unit_number == 1:
        # Special case for 21, 31, ..., 61, (30 and 1)
        unit_text = 'et-' + unit_text
    return ten_text + '-' + unit_text

def only_zeros_left(number):
    """Test if only zeros left in number

    Parameters
    ----------
    number : str
        Number to test

    Returns
    -------
    bool
        True if number contains only zero
    """
    return '0' * len(number) == number

def convert_hundreds(number, trailing):
    """Convert number with three digits

    Parameters
    ----------
    number : str
        3 digits number

    Returns
    -------
    str
        Text version of the number
    """
    result = ''
    if number[0] == '0':
        return ''
    if number[0] == '1':
        result = simple_numbers['100']
    else:
        result = simple_numbers[number[0]] + '-cent'
    if only_zeros_left(trailing) and only_zeros_left(number[1:]):
        # Only plural if no trailing digits
        result += 's'
    return result

def concat_data(current, data_to_add):
    """Concat number with previous text

    Parameters
    ----------
    current : str
        Current state of the text
    data_to_add : str
        Data to add at the end of the text

    Returns
    -------
    str
        Text version of the number
    """
    if current == '':
        return data_to_add
    if data_to_add != '':
        return current + '-' + data_to_add
    return current
