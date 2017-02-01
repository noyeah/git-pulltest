# -*- coding: utf-8 -*-

"""
URL: http://www.codewars.com/kata/54474afb46324f45190000a5

Description:
In this Kata you will create a function that takes a list of lists as an input and returns a flat list.

Example:
flatten [[1,2],[3,4]] == [1,2,3,4]
flatten [[1],[2],[3],[4]] == [1,2,3,4]
"""

# l = [[1],[2],[3],[4]]
# l = [[1,2],[3,4]]
l = [1, 2, 3, 4, 1, 2, 3, 4]
result = []


def flatten(l):
    for i in l:
        if type(i) == list:
            for j in i:
                if j not in result:
                    result.append(j)
        elif i not in result:
            result.append(i)
    return result


print flatten(l)

"""
Result:
[1, 2, 3, 4]
python2 인듯??
"""
