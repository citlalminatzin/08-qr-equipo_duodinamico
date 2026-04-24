#!/usr/bin/env python

"""
Realiza la factorización QR de una matriz
"""

from gram_schmidt import gm, transpose, dot

def qr(M: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    """
    Calcula la factorización QR de una matriz cuadrada M
    usando el proceso de Gram-Schmidt.
    """

    n = len(M)

    if n == 0 or any(len(row) != n for row in M):
        raise ValueError("La matriz debe ser cuadrada")

    # Obtenemos las columnas de la matriz M
    columnas = transpose(M)

    # Aquí se guardarán las columnas ortonormales de Q
    q_columnas = []

    # Matriz R inicializada con ceros
    R = [[0.0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        v = columnas[j][:]

        for i in range(j):
            R[i][j] = dot(q_columnas[i], columnas[j])
            v = [v[k] - R[i][j] * q_columnas[i][k] for k in range(n)]

        R[j][j] = norm(v)

        if abs(R[j][j]) < 1e-12:
            raise ValueError("La matriz tiene columnas linealmente dependientes")

        q_j = [v[k] / R[j][j] for k in range(n)]
        q_columnas.append(q_j)

    # Q se forma colocando las columnas ortonormales como columnas de la matriz
    Q = transpose(q_columnas)

    return Q, R