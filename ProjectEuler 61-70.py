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


def generateTriangleNums(lower_limit, upper_limit):
    """asssumes lower limits and upper_limit are ints,
    the lowest and highest values (inclusive) to be considered
    returns a list of ints, the triangle numbers between lower_limit and upper_limit,
    in acending order
    """
    triangle_num_list = []
    i = int(lower_limit**0.5)
    triangle_num = 0
    while triangle_num <= upper_limit:
        triangle_num = int(i*(i+1)/2)
        if triangle_num >= lower_limit and triangle_num <= upper_limit:
            triangle_num_list.append(triangle_num)
        triangle_num = int(i*(i+1)/2)
        i += 1
    return triangle_num_list


# generateTriangleNums(0, 100)


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
        square_num = int(i**2)
        if square_num >= lower_limit and square_num <= upper_limit:
            square_num_list.append(square_num)
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
    i = int((lower_limit**0.5)/2)
    pentagon_num = 0
    while pentagon_num <= upper_limit:
        pentagon_num = int(i*((3*i)-1)/2)
        if pentagon_num >= lower_limit and pentagon_num <= upper_limit:
            pentagon_num_list.append(pentagon_num)
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
    i = int((lower_limit**0.5)/2)
    hexagon_num = 0
    while hexagon_num <= upper_limit:
        hexagon_num = int(i*((2*i)-1))
        if hexagon_num >= lower_limit and hexagon_num <= upper_limit:
            hexagon_num_list.append(hexagon_num)
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
    i = int((lower_limit**0.5)/2)
    heptagon_num = 0
    while heptagon_num <= upper_limit:
        heptagon_num = int(i*((5*i)-3)/2)
        if heptagon_num >= lower_limit and heptagon_num <= upper_limit:
            heptagon_num_list.append(heptagon_num)
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
    i = int((lower_limit**0.5)/2)
    octagon_num = 0
    while octagon_num <= upper_limit:
        octagon_num = int(i*((3*i)-2))
        if octagon_num >= lower_limit and octagon_num <= upper_limit:
            octagon_num_list.append(octagon_num)
        i += 1
    return octagon_num_list


# print(generateOctagonNums(1, 100))


def isCyclic2Digit(num1, num2):
    """assumes num1 and num2 are ints
    returns True if the last 2 digits of num1 are the same as the first 2 digits of num2,
    else returns False
    """
    return (str(num1)[-2] + str(num1)[-1]) == str(num2)[:2]


# print(isCyclic2Digit(1994, 9433))

def get_permutations(sequence):
    '''
    Assumes sequence is an arbitrary string and non-empty
    Returns: a list of strings, all the permutations of sequence
    Example: get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    note: do not depend on order of the output list
    '''
    permutations_of_sequence = []
    permutations_of_cutdown_sequence = []
    # define recursive behaviour
    # for sequence of len(n), case is sequence[0] and sequence[1:n]
    if len(sequence) > 1:
        first_char_sequence = sequence[0]
        cutdown_sequence = sequence[1:]
        # find recursions of cutdown_sequence
        if len(cutdown_sequence) > 1:
            permutations_of_cutdown_sequence = get_permutations(sequence[1:])
        # base case
        # add first_char_sequence to all recursions of cutdown_sequence
        for i in range(len(sequence)):
            holding_string = cutdown_sequence[:i] + first_char_sequence\
                + cutdown_sequence[i:]
            permutations_of_sequence += [holding_string]
        # loop over each item in permutations_of_cutdown_sequence
        if len(permutations_of_cutdown_sequence) > 1:
            for ele in range(len(permutations_of_cutdown_sequence)):
                new_cutdown_sequence = permutations_of_cutdown_sequence[ele]
                for i in range(len(sequence)):
                    holding_string = new_cutdown_sequence[:i] +\
                        first_char_sequence + new_cutdown_sequence[i:]
                    permutations_of_sequence += [holding_string]
    # remove duplicates from permutations_of_sequence
    return list(dict.fromkeys(permutations_of_sequence))


def cyclicalFigurateNums():
    """returns an int, the sum of the set of 6 numbers where the numbers are:
        cyclic
        4 digits
        each is a polygonal number from triangle to octagon
    """
    # initialize lists of 4 digit polygon numbers
    triangle_nums_list = generateTriangleNums(1000, 10000)
    square_nums_list = generateSquareNums(1000, 10000)
    pentagon_num_list = generatePentagonNums(1000, 10000)
    hexagon_num_list = generateHexagonNums(1000, 10000)
    heptagon_num_list = generateHeptagonNums(1000, 10000)
    octagon_num_list = generateOctagonNums(1000, 10000)
    polygon_nums_list_list = [triangle_nums_list, square_nums_list, pentagon_num_list,
                              hexagon_num_list, heptagon_num_list, octagon_num_list]
    # permutations of polygon lists
    polygon_permutations = get_permutations("012345")
    # generate list
    for permutation in polygon_permutations:
        reordered_polygon_nums_list_list = []
        for digit in permutation:
            reordered_polygon_nums_list_list.append(polygon_nums_list_list[int(digit)])
        # test for cyclic  on each polygon list
        for num_0 in reordered_polygon_nums_list_list[0]:
            num_0_start = int((str(num_0)[:2]))
            num_0_end = int((str(num_0)[2:]))
            for num_1 in reordered_polygon_nums_list_list[1]:
                num_1_start = int((str(num_1)[:2]))
                num_1_end = int((str(num_1)[2:]))
                if num_0_end == num_1_start:
                    for num_2 in reordered_polygon_nums_list_list[2]:
                        num_2_start = int((str(num_2)[:2]))
                        num_2_end = int((str(num_2)[2:]))
                        if num_1_end == num_2_start:
                            for num_3 in reordered_polygon_nums_list_list[3]:
                                num_3_start = int((str(num_3)[:2]))
                                num_3_end = int((str(num_3)[2:]))
                                if num_2_end == num_3_start:
                                    for num_4 in reordered_polygon_nums_list_list[4]:
                                        num_4_start = int((str(num_4)[:2]))
                                        num_4_end = int((str(num_4)[2:]))
                                        if num_3_end == num_4_start:
                                            for num_5 in reordered_polygon_nums_list_list[5]:
                                                num_5_start = int((str(num_5)[:2]))
                                                num_5_end = int((str(num_5)[2:]))
                                                if num_4_end == num_5_start and num_5_end == num_0_start:
                                                    num_set = (num_0, num_1, num_2,
                                                               num_3, num_4, num_5)
                                                    print(num_set)
    return sum(num_set)

# print(cyclicalFigurateNums())


"""
Problem 62
The cube, 41063625 (345**3), can be permuted to produce two other cubes:
    56623104 (384**3) and 66430125 (405**3).
    41063625 is the smallest cube which has
    exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def isPermutation(string1, string2):
    """assumes string1 and string 2 are strings
    returns True if string1 and string2 are permutations of each other, else False
    """
    char_list1 = sorted(string1)
    char_list2 = sorted(string2)
    return char_list1 == char_list2


# print(isPermutation("art", "rat"))
# print(isPermutation("artt", "rat"))
# print(isPermutation("cats", "art"))


def cubicPermutationsv1():
    """returns an int,
    the smallest cube that has five permutations of its digits that are cubes
    very slow, not recommended
    """
    cubes_list = []
    for i in range(1000000):
        cube = i**3
        cube_permutations = get_permutations(str(cube))
        cube_permutations_count = 0
        for permutation in cube_permutations:
            if permutation in cubes_list:
                cube_permutations_count += 1
            if cube_permutations_count == 5:
                return cube
        cubes_list.append(str(cube))


# cubicPermutationsv1()  # force stoped after over 10 minutes of running


def sortStrictlyIncreasing(num):
    """assumes num is an int
    returns an int, the num with it's digits in strictly increasing order
    e.g. sortStrictlyIncreasing(5284) -> 2458
    """
    return "".join(sorted([digit for digit in str(num)]))


# print(sortStrictlyIncreasing(5284))


def cubicPermutations():
    """returns an int,
    the smallest cube that has five permutations of its digits that are cubes
    """
    cubes_dict = {}
    for i in range(1000000):
        cube = i**3
        strictly_increasing_cube = sortStrictlyIncreasing(cube)
        if strictly_increasing_cube in cubes_dict:
            cubes_dict[strictly_increasing_cube].append(cube)
            if len(cubes_dict[strictly_increasing_cube]) == 5:
                return min(cubes_dict[strictly_increasing_cube])
        else:
            cubes_dict[strictly_increasing_cube] = [cube]


# print(cubicPermutationsv())


"""
problem 63
The 5-digit number, 16807=7**5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""


def powerfulDigitCounts():
    """returns an int,
    the number of n-digit positive integers exist which are also an nth power"""
    result = 0
    upper_bound = 10
    for n in range(1, 1000000000):  # arbitrarily high loop, will self-stop
        lower_bound = math. ceil(10**((n-1)/n))
        result += 10 - lower_bound
        if lower_bound >= upper_bound:
            return result


# print(powerfulDigitCounts())


"""
problem 63
Exactly four continued fractions, for N<13 have an odd period.

How many continued fractions for N<10000 have an odd period?
"""
