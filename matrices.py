A = [[1, 0, 1], [-1, 1, 0]]
print(A)

T = ((1, 0, 1), (-1, 1, 0))
print(T)


def MultiplieLigne(A, i, alpha):
    for k in range(len(A[i])):
        A[i][k] *= alpha


A = [[1, 0, 1], [-1, 1, 0]]
print("MultiplieLigne")
print(A)
MultiplieLigne(A, 1, 5)
print(A)


def MultiplieColonne(A, j, alpha):
    for k in range(len(A)):
        A[k][j] *= alpha


A = [[1, 0, 1], [-1, 1, 0]]
print("MultiplieColonne")
print(A)
MultiplieColonne(A, 0, 3)
print(A)


def AjouteLigne(A, i, j, alpha):
    for k in range(len(A[i])):
        A[i][k] += alpha*A[j][k]


A = [[1, 0, 1], [-1, 1, 0]]
print("AjouteLigne")
print(A)
AjouteLigne(A, 1, 0, 2)
print(A)


def AjouteColonne(A, i, j, alpha):
    for k in range(len(A)):
        A[k][i] += alpha*A[k][j]


A = [[1, 0, 1], [-1, 1, 0]]
print("AjouteColonne")
print(A)
AjouteColonne(A, 1, 0, 2)
print(A)


def EchangeLigne(A, i, j):
        A[i], A[j] = A[j], A[i]


A = [[1, 0, 1], [-1, 1, 0]]
print("EchangeLigne")
print(A)
EchangeLigne(A, 0, 1)
print(A)


def EchangeColonne(A, i, j):
    for k in range(len(A)):
        A[k][i], A[k][j] = A[k][j], A[k][i]


A = [[1, 0, 1], [-1, 1, 0]]
print("EchangeColonne")
print(A)
EchangeColonne(A, 0, 1)
print(A)


import numpy as np
print("#"*30)


def MultiplieLigne(A, i, alpha):
    for k in range(len(A[i])):
        A[i][k] *= alpha


A = [[1, 0, 1], [-1, 1, 0]]
print("MultiplieLigne")
A = np.array([[1, 0, 1], [-1, 1, 0]])
MultiplieLigne(A, 1, 5)
print(A)


def MultiplieColonne(A, j, alpha):
    for k in range(len(A)):
        A[k][j] *= alpha


A = [[1, 0, 1], [-1, 1, 0]]
print("MultiplieColonne")
A = np.array([[1, 0, 1], [-1, 1, 0]])
MultiplieColonne(A, 0, 3)
print(A)


def AjouteLigne(A, i, j, alpha):
    for k in range(len(A[i])):
        A[i][k] += alpha*A[j][k]


A = [[1, 0, 1], [-1, 1, 0]]
print("AjouteLigne")
A = np.array([[1, 0, 1], [-1, 1, 0]])
AjouteLigne(A, 1, 0, 2)
print(A)


def AjouteColonne(A, i, j, alpha):
    for k in range(len(A)):
        A[k][i] += alpha*A[k][j]


A = [[1, 0, 1], [-1, 1, 0]]
print("AjouteColonne")
A = np.array([[1, 0, 1], [-1, 1, 0]])
AjouteColonne(A, 1, 0, 2)
print(A)


def EchangeLigne(A, i, j):
    for k in range(len(A[i])):
        A[i][k], A[j][k] = A[j][k], A[i][k]


A = [[1, 0, 1], [-1, 1, 0]]
print("EchangeLigne")
A = np.array([[1, 0, 1], [-1, 1, 0]])
EchangeLigne(A, 0, 1)
print(A)


def EchangeColonne(A, i, j):
    for k in range(len(A)):
        A[k][i], A[k][j] = A[k][j], A[k][i]


A = [[1, 0, 1], [-1, 1, 0]]
print("EchangeColonne")
A = np.array([[1, 0, 1], [-1, 1, 0]])
EchangeColonne(A, 0, 1)
print(A)