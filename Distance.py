# m = x.lenght
# n = y.length
# siano c[0,...,m 0,..n] e op[0...,m 0...n] 2 tabelle
# for i = 0 to m
# c[i,0] = i * cost(delete)
# op[i,0] = Delete
# for j = 0 to n
# c[j,0] = j*cost(Insert)
# op[j,0] = insert
import numpy as np

X = raw_input("Inserisci parola: ")
Y = raw_input("Inserisci seconda parola: ")
sh = {len(X) * len(Y)}


def editDistance(X, Y):
    m = len(X)
    n = len(Y)
    c = np.zeros([m + 1, n + 1], dtype=int)
    for i in range(m + 1):
        c[i, 0] = i
    for i in range(n + 1):
        c[0, i] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            c[i, j] = 1000000
            if X[i - 1] == Y[j - 1]:
                c[i, j] = c[i - 1, j - 1] + 0  # costo della copia
            if X[i - 1] != Y[j - 1] and (c[i - 1, j - 1] + 1) < c[i, j]:
                c[i, j] = c[i - 1, j - 1] + 1  # costo replace
            if i >= 2 and j >= 2 and X[i - 1] == Y[j - 2] and X[i - 2] == Y[j - 1] and (c[i - 2, j - 2] + 2) < c[i, j]:  # 2 costo scambio
                c[i, j] = c[i - 2, j - 2] + 2
            if c[i - 1, j] + 1 < c[i, j]:
                c[i, j] = c[i - 1, j] + 1
            if (c[i, j - 1] + 1) < c[i, j]:
                c[i, j] = c[i, j - 1] + 1
    return c


print editDistance(X, Y)
