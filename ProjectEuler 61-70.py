# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:39:52 2021

@author: catal
"""

import pdb
import math
import timeit
from functools import reduce
from itertools import count, islice
import itertools
import string
import regex as re
import icecream

"""
problem 61

Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers
are all figurate (polygonal) numbers and are generated by the following formulae:

Triangle	 	P(3,n)=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P(4,n)=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P(5,n)=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P(6,n)=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P(7,n)=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P(8,n)=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281,
has three interesting properties.

The set is cyclic, in that the last two digits of each number is
the first two digits of the next number (including the last number with the first).
Each polygonal type:
    triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882),
is represented by a different number in the set.
This is the only set of 4-digit numbers with this property.

Find the sum of the only ordered set of six cyclic 4-digit numbers
for which each polygonal type:
    triangle, square, pentagonal, hexagonal, heptagonal, and octagonal,
is represented by a different number in the set.
"""

# Goal= sum of set of 6 nums that are:
#     4 digits
#     cyclic
#     triangle, square, pentagonal, hexagonal, heptagonal, and octagonal

# brute force plan to find set:
#     make lists of 4 digit polygonal nums
#     iterate over triangle num, for each:
#         take last 2 digits of triangle num
#         iterate over square nums, for each:
#             if last 2 digits of triangle match first 2 digits of square num:
#                 iterate over pentagon nums, for each:
#                     if last 2 digits of square match first 2 digits of pentagon num:
#                         iterate over hexagon nums, for each:
#                             if last 2 digits of pentagon match first 2 digits of hexagon num:
#                                 iterate over heptagon nums, for each:
#                                     if last 2 digits of hexagon match first 2 digits of heptagon num:
#                                         iterate over octagon nums, for each:
#                                             if last 2 digits of heptagon match first 2 digits of octagon num:
#                             return sum(set with 6 nums)


def generateTriangleNums(lower_limit, upper_limit):
    """asssumes lower limits and upper_limit are ints,
    the lowest and highest values (inclusive) to be considered
    returns a list of ints, the triangle numbers between lower_limit and upper_limit,
    in acending order
    """
    triangle_num_list = []
    i = int(lower_limit**0.5)
    triangle_num = 1
    while triangle_num <= upper_limit:
        if triangle_num >= lower_limit:
            triangle_num_list.append(triangle_num)
        triangle_num = int(i*(i+1)/2)
        i += 1
    return triangle_num_list


# generateTriangleNums(20, 100)


def generateSquareNums(lower_limit, upper_limit):
    """asssumes lower limits and upper_limit are ints,
    the lowest and highest values (inclusive) to be considered
    returns a list of ints, the square numbers between lower_limit and upper_limit,
    in acending order
    """
    square_num_list = []
    i = int(lower_limit**0.5)
    square_num = 0
    while square_num <= upper_limit:
        if square_num >= lower_limit:
            square_num_list.append(square_num)
        square_num = int(i**2)
        i += 1
    return square_num_list


# print(generateSquareNums(1, 100))
# print(generateSquareNums(44, 100))


def generatePentagonNums(lower_limit, upper_limit):
    """asssumes lower limits and upper_limit are ints,
    the lowest and highest values (inclusive) to be considered
    returns a list of ints, the pentagon numbers between lower_limit and upper_limit,
    in acending order
    """
    pentagon_num_list = []
    i = int(lower_limit**0.5)
    pentagon_num = 0
    while pentagon_num <= upper_limit:
        if pentagon_num >= lower_limit:
            pentagon_num_list.append(pentagon_num)
        pentagon_num = int(i*((3*i)-1)/2)
        i += 1
    return pentagon_num_list


# print(generatePentagonNums(1, 100))
# print(generatePentagonNums(17, 200))


def generateHexagonNums(lower_limit, upper_limit):
    """asssumes lower limits and upper_limit are ints,
    the lowest and highest values (inclusive) to be considered
    returns a list of ints, the hexagon numbers between lower_limit and upper_limit,
    in acending order
    """
    hexagon_num_list = []
    i = int(lower_limit**0.5)
    hexagon_num = 0
    while hexagon_num <= upper_limit:
        if hexagon_num >= lower_limit:
            hexagon_num_list.append(hexagon_num)
        hexagon_num = int(i*((2*i)-1))
        i += 1
    return hexagon_num_list


# print(generateHexagonNums(1,100))


def generateHeptagonNums(lower_limit, upper_limit):
    """asssumes lower limits and upper_limit are ints,
    the lowest and highest values (inclusive) to be considered
    returns a list of ints, the heptagon numbers between lower_limit and upper_limit,
    in acending order
    """
    heptagon_num_list = []
    i = int(lower_limit**0.5)
    heptagon_num = 0
    while heptagon_num <= upper_limit:
        if heptagon_num >= lower_limit:
            heptagon_num_list.append(heptagon_num)
        heptagon_num = int(i*((5*i)-3)/2)
        i += 1
    return heptagon_num_list


# print(generateHeptagonNums(1, 100))
# print(generateHeptagonNums(1000, 10000))


def generateOctagonNums(lower_limit, upper_limit):
    """asssumes lower limits and upper_limit are ints,
    the lowest and highest values (inclusive) to be considered
    returns a list of ints, the octagon numbers between lower_limit and upper_limit,
    in acending order
    """
    octagon_num_list = []
    i = int(lower_limit**0.5)
    octagon_num = 0
    while octagon_num <= upper_limit:
        if octagon_num >= lower_limit:
            octagon_num_list.append(octagon_num)
        octagon_num = int(i*((3*i)-2))
        i += 1
    return octagon_num_list


# print(generateOctagonNums(1, 100))


def cyclicalFigurateNums():
    """returns an int, the sum of the set of 6 numbers where the numbers are:
        cyclic
        4 digits
        each is a polygonal number from triangle to octagon
    """
    pass


