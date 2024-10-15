from datetime import datetime, date, time
import bisect
import re

def main():
    tup = 4, 5, 6
    print(tup)

    n_tup = (4, 5, 6), (7, 8)
    print(n_tup)

    l = [4, 0, 2]
    print(l)
    tup = tuple(1)
    print(tup)
    print(tup[0])

    tup = tuple(["foo", [1, 2], True])
    print(tup)
    tup[2] = False
    tup[1].append(3)
    print(tup)

    tup = (4, 5, 6)
    a, b, c = tup
    print(b)
    print(c)

    a_list = [2, 3, 7, None]
    tup = ("foo", "bar", "baz")
    print(a_list)
    print(tup)

    b_list = list(tup)
    print(b_list)
    b_list[1] = "test"
    print(b_list)

    b_list.append("dwarf")
    print(b_list)
    b_list.insert(2, "red")
    print(b_list)
    print("dwarf" in b_list)
    print("dwarf" not in b_list)

    a = [7, 2, 5, 1, 3]
    a.sort()
    print(a)
    b = ["saw", "small", "He", "foxes", "six"]
    b.sort(key=len)
    print(b)

    c = [1, 2, 2, 2, 3, 4, 7]
    ret = bisect.bisect(c, 5)
    print(ret)
    bisect.insort(c, 6)
    print(c)

    seq = [7, 2, 3, 7, 5, 6, 0, 1]
    print(seq[1:5])
    seq[3:4] = [6, 3]
    print(seq)
    print(seq[:5])
    print(seq[3:])
    print(seq[-4:])
    print(seq[-6:-2])

    some_list = ["foo", "bar", "baz"]
    mapping = {}
    for i, v in enumerate(some_list):
        mapping[v] = i
    print(mapping)

    l = sorted([7, 1, 2, 6, 0, 3, 2])
    print(l)

    seq1 = ["foo", "bar", "baz"]
    seq2 = ["one", "two", "three"]
    zipped = zip(seq1, seq2)
    print(list(zipped))

    l = list(reversed(range(10)))
    print(l)

    d1 = {'a' : 'some_value', 'b' : [1, 2, 3, 4]}
    # print(d1)

    d1[7] = 'an integer'
    # print(d1)
    # print(d1['b'])
    d1[5] = 'some value'
    print(d1)
    del d1[5]
    print(d1)
    d1.pop('b')
    print(d1)

    d1 = {'a' : 'some value', 7 : 'an integer'}
    d1.update({'b' : 'foo', 'c' : 12})
    print(d1)

    key_list = ['a', 'b', 'c']
    value_list = ["foo", "bar", "baz"]
    mapping = {}
    for key, value in zip(key_list, value_list):
        mapping[key] = value
    print(mapping)

    default = "default"
    some_dict = {'a' : 'some value', 7 : 'an integer'}
    value = some_dict.get('a', default)
    print(value)

    s = set([2, 2, 2, 1, 3, 3])
    print(s)
    s = {2, 2, 2, 1, 3, 3}
    print(s)

    a = {1, 2, 3, 4, 5}
    b = {3, 4, 5, 6, 7, 8}

    # a | b
    s = a.union(b)
    print(s)
    # a & b
    s = a.intersection(b)
    print(s)
    # a - b
    s = a.difference(b)
    print(s)

    def my_func(x, y, z = 1.5):
        if z > 1:
            return z * (x + y)
        else:
            return z / (x + y)
    ret = my_func(4, 6, 3.5)
    print(ret)
    ret = my_func(10, 20)
    print(ret)
    ret = my_func(10, 20, -1)
    print(ret)

    def func():
        a = []
        for j in range(5):
            a.append(j)
        print(a)
    func()
    b = []
    def func2():
        for j in range(5):
            b.append(j)
        print(b)
    func2()
    c = None
    def func3():
        global c
        c = []
        for j in range(5):
            c.append(j)
        print(c)
    func3()

    def f():
        a = 5
        b = 6
        c = 7
        return a, b, c
    
    l, m, n = f()
    print(l, m, n)

    states = ['Alabama', 'Georgia!', 'Georgia', 'georgia', 'FlOriDa', 'south carolina##', 'West virginia?']
    def clean_str(strings):
        ret = []
        for value in strings:
            value = value.strip()
            value = re.sub('[!#?]', '', value)
            value = value.title()
            ret.append(value)
        return ret
    
    s = clean_str(states)
    print(s)

    def short_func(x):
        return x * 2
    z = 2
    ret1 = short_func(z)
    ret2 = (lambda x : x * 2)(z)
    print(ret1, ret2)

    def attempt_float(x):
        try:
            return float(x)
        except ValueError:
            return x
        ret = attempt_float('1.23')
        print(ret)
        ret = attempt_float('something')
        print(ret)
    
    if __name__ == '__main__' : # main()
        main()