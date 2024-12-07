import re

"""
Um endereço de e-mail válido atende aos seguintes critérios:

É composto por nome de usuário, nome de domínio e extensão reunidos neste formato: nomedeusuário@domínio.extensão
O nome de usuário começa com um caractere alfabético em inglês e quaisquer caracteres subsequentes consistem em um ou mais dos seguintes: caracteres alfanuméricos, -,. e _.
O domínio e a extensão contêm apenas caracteres alfabéticos do inglês.
A extensão tem comprimento de 1, 2, ou 3 caracteres.
Dados pares de nomes e endereços de e-mail como entrada, imprima cada par de nome e endereço de e-mail com um endereço de e-mail válido em uma nova linha.
"""

email_pattern = r'^<[a-zA-Z]{1}[\w.-]*\@[a-zA-Z]+\.[a-z]{1,3}>$'

n = int(input())

for _ in range(n):
    name, email_adress = input().split()
    if re.fullmatch(email_pattern, email_adress):
        print(f'{name} {email_adress}')

"""
sample input
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

sample output
DEXTER <dexter@hotmail.com>
"""