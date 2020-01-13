"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

N = 10
LINE = ''

for i in range(32, 128):
    LINE = LINE + '{: ^7}'.format(f'{i}({chr(i)})')
    N -= 1
    if N < 0:
        print(LINE)
        LINE = ''
        N = 10
else:
    if N != 10:
        print(LINE)
        print('----------------------------------------------------------------')


N = 10
LINE = ''
SYM = 32


def ascii_simbols(n, line, sym):

    line = line + '{: ^7}'.format(f'{sym}({chr(sym)})')
    n -= 1
    sym += 1

    if n < 0:
        print(line)
        line = ''
        n = 10

    if sym > 127:
        print(line)
        line = ''
        return

    ascii_simbols(n, line, sym)

ascii_simbols(N, LINE, SYM)