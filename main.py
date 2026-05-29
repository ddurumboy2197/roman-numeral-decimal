def roman_to_decimal(roman_num):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal_num = 0
    for i in range(len(roman_num)):
        if i > 0 and roman_dict[roman_num[i]] > roman_dict[roman_num[i - 1]]:
            decimal_num += roman_dict[roman_num[i]] - 2 * roman_dict[roman_num[i - 1]]
        else:
            decimal_num += roman_dict[roman_num[i]]
    return decimal_num

print(roman_to_decimal('III'))  # 3
print(roman_to_decimal('IV'))  # 4
print(roman_to_decimal('IX'))  # 9
print(roman_to_decimal('LVIII'))  # 58
print(roman_to_decimal('MCMXCIV'))  # 1994
