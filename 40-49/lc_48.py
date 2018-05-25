# !/usr/bin/env python
# -*-coding: utf-8 -*-


def rotate(matrix):
    matrix_length = len(matrix)
    for i in range(1, matrix_length):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(0, matrix_length):
        matrix[i] = list(reversed(matrix[i]))
