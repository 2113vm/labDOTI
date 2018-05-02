import collections
import re


ALHAVIT = set(re.findall('[а-яА-Я]', case))
ALHAVIT.add(' ')
ALHAVIT = list(ALHAVIT)


with open('case5', 'r', encoding='1251') as f:
    case = f.read()


def get_list_ngrams(lenght, case):
    return list({case[i: i + lenght] for i in range(0, len(case)-lenght)})


def find_indexs_pattern(pattern, case=case):
    return [pat.span()[0] for pat in re.finditer(pattern, case)]    


def get_good_ngrams(lenght):
    d = {pattern: find_indexs_pattern(pattern, case) for pattern in get_list_ngrams(lenght, case)}
    return list(filter(lambda item: len(item[1]) > 1, d.items()))


r = get_good_ngrams(9)


res = [get_good_ngrams(l) for l in range(3, 10)]


def minus(lst):
    return [lst[i] - lst[i - 1] for i in range(1, len(lst))]


res_minus = [[(pat[0], minus(pat[1])) for pat in r] for r in res]


lenghts = []
[[lenghts.extend(_) for _ in i] for i in [[r[1]for r in res_] for res_ in res_minus]]


c = collections.Counter(lenghts)


sorted(c.items(), key=lambda item: item[1], reverse=True)


def count(word, s):
    return collections.Counter(re.findall(word, s))[word]


def I(s):
    n = len(s)
    return sum([count(alh, s)*(count(alh, s) - 1) / (n * (n - 1)) for alh in ALHAVIT])


I(case)


def get_n_word(n):
    return ''.join([case[i] for i in range(0, len(case), n)])


I(get_n_word(20))


min_ = 999
min_n = 0
for i in range(1, int(len(case) / 2)):
    if abs(I(get_n_word(i)) - 0.0553) < min_:
        min_ = abs(I(get_n_word(i)) - 0.0553)
        min_n = i
        

min_n

