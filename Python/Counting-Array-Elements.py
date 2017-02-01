# -*- coding: utf-8 -*-

"""
URL: http://www.codewars.com/kata/5569b10074fe4a6715000054

Description:
Write a function that takes an array and counts the number of each unique element present.
"""

array = ['Hayato Jin', 'Benkei Kurama', 'Michiru Saotome', 'Hayato Jin', 'Benkei Kurama', 'Benkei Kurama',
         'Benkei Kurama', 'Hayato Jin', 'Saotome-agase', 'Musashi Tomoe', 'Musashi Tomoe', 'Michiru Saotome',
         'Benkei Kurama', 'Benkei Kurama', 'Ryoma Nagare', 'Michiru Saotome', 'Saotome-agase', 'Benkei Kurama',
         'Hayato Jin']


def count(array):
    num = {}
    for item in array:
        num[item] = array.count(item)

    return num

print count(array)

# # Best Solution:
# from collections import Counter as count
# print dict(count(array))

"""
Result:
{'Hayato Jin': 4, 'Musashi Tomoe': 2, 'Ryoma Nagare': 1, 'Saotome-agase': 2, 'Michiru Saotome': 3, 'Benkei Kurama': 7}
python2
"""
