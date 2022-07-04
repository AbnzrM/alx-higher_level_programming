#!/usr/bin/python3
# 6-print_matrix_integer.py
# Brennan D Baraban <375@holbertonschool.com>

def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    else:
        for row in matrix:
            for column in row:
                print('{:d}'.format(column), end=' '
                      if column != row[-1] else '\n')
