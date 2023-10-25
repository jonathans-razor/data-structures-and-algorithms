import sys

def roman_to_integer(roman):
    roman = roman.upper()
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(roman)):
        if i > 0 and roman_dict[roman[i]] > roman_dict[roman[i - 1]]:
            if roman[i - 1] + roman[i] not in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                print("Invalid Roman numeral")
                return None
            result += roman_dict[roman[i]] - 2 * roman_dict[roman[i - 1]]
        else:
          # This is the cummulative operation.
          result += roman_dict[roman[i]]
    return result

if len(sys.argv) < 2:
    print("- Parameter(s) expected.")
    sys.exit(1)

print(roman_to_integer(sys.argv[1]))