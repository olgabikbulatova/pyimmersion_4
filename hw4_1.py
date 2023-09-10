# Напишите функцию для транспонирования матрицы
import random

def trans_matrix(data: list) -> list:
    trans_mat = [[0 for j in range(len(data))] for i in range(len(data[0]))]
    for i in range(len(data)):
        for j in range(len(data[0])):
            trans_mat[j][i] = data[i][j]
    return trans_mat


column = int(input('введите колво стобцов'))
lines = int(input('введите кол-во строк'))
matrix = [[random.randint(-10, 10) for _ in range(column)] for i in range(lines)]
print(matrix)
print(trans_matrix(matrix))