"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque

string = ('of all the things i\'ve lost, i miss my minde the most!')
#string = "beep boop beer!"


def binary_tree(s):

    s = Counter(list(s))
    s = deque(sorted(s.items(), key=lambda x: x[1]))

    if len(s) != 1:
        while len(s) > 1:
            weight = s[0][1] + s[1][1]
            node = {0: s.popleft()[0],
                    1: s.popleft()[0]}


            for num, item in enumerate(s):
                if weight > item[1]:
                    continue
                else:
                    s.insert(num, (node, weight))
                    break
            else:
                s.append((node, weight))
    else:
        weight = s[0][1]
        node = {0: s.popleft()[0],
                1: None}
        s.append((node, weight))

    return s[0][0]


tree = binary_tree(string)
coding_valuse = {}


def haffman_encoding(btree, code=''):

    if not isinstance(btree, dict):
        coding_valuse[btree] = code
    else:
        haffman_encoding(btree[0], code=f'{code}0')
        haffman_encoding(btree[1], code=f'{code}1')


haffman_encoding(tree)

for i in string:
    print(coding_valuse[i], end=' ')
print(coding_valuse)
