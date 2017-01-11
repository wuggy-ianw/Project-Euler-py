# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import collections

units_to_text_simple = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine' }
units_to_text_teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9: 'nineteen' }

tens_to_text = {0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

def digits_to_text_tens_and_units(tens, units):
    if tens == 0 and units == 0:
        return ''
    if tens == 1:
        return units_to_text_teens[units]

    tens_string = tens_to_text[tens]
    units_string = units_to_text_simple[units]

    result = tens_string + (' ' if tens_string!='' and units_string!='' else '') + units_string
    return result

def pluralise(n, singular):
    if n == 1:
        return singular
    return singular + 's'

def digits_to_text(thousands, hundreds, tens, units):
    thousands_string = units_to_text_simple[thousands] + ' ' + 'thousand' if thousands != 0 else ''
    hundreds_string = units_to_text_simple[hundreds] + ' ' + 'hundred' if hundreds != 0 else ''
    tens_unit_string = digits_to_text_tens_and_units(tens, units)

    thousands_hundreds_string = thousands_string + (' ' if thousands_string!='' and hundreds_string!='' else '') + hundreds_string
    result = thousands_hundreds_string + (' and ' if thousands_hundreds_string!='' and tens_unit_string!='' else '') + tens_unit_string

    return result



letter_counter = collections.Counter()
for i in range(1,1001):
    digits = [int(x) for x in str(i).zfill(4)]
    digit_text = digits_to_text(*digits)
    print(digit_text)

    for s in digit_text:
        if s == ' ':
            continue
        letter_counter[s] += 1

print(sum(letter_counter.values()))

