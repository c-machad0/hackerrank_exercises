import re

n = int(input())

# ^[789] - indica que o primeiro caractere da string seja 7, 8 ou 9
# [0-9]{9} - exige que haja exatamente 9 digitos que estejam entre 0 e 9
# $ indica o final da string, garantindo que não tenha mais de 10 digitos
pattern_validate = r'^[789]{1}[0-9]{9}$'

for _ in range(n):
    number = input()
    validity = re.fullmatch(pattern_validate, number) # fullmatch aplica o padrão para toda string
    if validity:
        print('YES')
    else:
        print('NO')


"""
sample input
2
9587456281
1252478965

sample output
YES
NO
"""