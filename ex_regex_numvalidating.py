import re

regex_pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

# M -> Pode aparecer até 3x. Ex: 3000 = MMM
# (CM|CD|D?C{0,3}) -> Ou você tem CM (900) ou voce tem CD (400) ou voce tem D seguido de até 3 C(500-800)
# (XC|XL|L?X{0,3}) -> Ou voce tem XC (90) ou voce tem XL (40) ou voce tem L (50) seguido de até 3 X(50-80)
# (IX|IV|V?I{0,3}) -> Ou voce tem IX (9) ou voce tem IV (4) ou voce tem V(5) seguido de até 3I (5-8)

print(str(bool(re.fullmatch(regex_pattern, input()))))