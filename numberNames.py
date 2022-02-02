#!/usr/bin/env python3
number_str = input("Enter the number: ")
number_int = int(number_str)
number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}

def get_number_name(n):
    number_name = ""
    number_len = len(str(n))
    try:
        number_name += number_names[n]
    except KeyError:
        try:
            number_name += number_names[n - n%10] + number_names[n%10]
        except KeyError:

            if number_len == 3:
                number_name += number_names[int((str(n - n%100))[0])]+ " hundred " + (get_number_name(n%100) if (n%100 > 0) else "")
            if number_len == 4:
                number_name +=  number_names[int((str(n - n%1000))[0])]+ " thousand " + (get_number_name(n%1000) if (n%1000 > 0) else "")

    return number_name

print(get_number_name(number_int))