#!/usr/bin/env python

"""
Funciones auxiliares para álgebra lineal y el proceso de Gram-Schmidt.
"""


def dot(x: list[float], y: list[float]) -> float:
    """
    Calcula el producto punto entre dos vectores.
    """

    if len(x) != len(y):
        raise ValueError("Los vectores deben tener la misma dimensión")

    return sum(x[i] * y[i] for i in range(len(x)))


def transpose(M: list[list[float]]) -> list[list[float]]:
    """
    Devuelve la transpuesta de una matriz.
    """

    if len(M) == 0:
        return []

    return [list(col) for col in zip(*M)]


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    """
    Multiplica dos matrices A y B.
    """

    if len(A) == 0 or len(B) == 0:
        raise ValueError("Las matrices no pueden estar vacías")

    columnas_B = transpose(B)

    if len(A[0]) != len(B):
        raise ValueError("Las dimensiones de las matrices no son compatibles")

    resultado = []

    for fila in A:
        nueva_fila = []

        for columna in columnas_B:
            nueva_fila.append(dot(fila, columna))

        resultado.append(nueva_fila)

    return resultado


def matvec(A: list[list[float]], v: list[float]) -> list[float]:
    """
    Multiplica una matriz A por un vector v.
    """

    if len(A) == 0:
        raise ValueError("La matriz no puede estar vacía")

    if len(A[0]) != len(v):
        raise ValueError("Las dimensiones de la matriz y el vector no son compatibles")

    return [dot(fila, v) for fila in A]


def norm(x: list[float]) -> float:
    """
    Calcula la norma 2 de un vector.
    """

    return dot(x, x) ** 0.5


def proj(u: list[float], v: list[float]) -> list[float]:
    """
    Calcula la proyección del vector u sobre el vector v.
    """

    denominador = dot(v, v)

    if abs(denominador) < 1e-15:
        raise ValueError("No se puede proyectar sobre el vector cero")

    coeficiente = dot(u, v) / denominador

    return [coeficiente * elemento for elemento in v]


def normalize(u: list[float]) -> list[float]:
    """
    Normaliza un vector.
    """

    norma = norm(u)

    if abs(norma) < 1e-15:
        raise ValueError("No se puede normalizar el vector cero")

    return [elemento / norma for elemento in u]


def gm(M: list[list[float]]) -> list[list[float]]:
    """
    Aplica el proceso de Gram-Schmidt a las columnas de una matriz M
    y devuelve una matriz con columnas ortonormales.
    """

    columnas = transpose(M)
    columnas_ortonormales = []

    for columna in columnas:
        v = columna[:]

        for q in columnas_ortonormales:
            proyeccion = proj(v, q)
            v = [v[i] - proyeccion[i] for i in range(len(v))]

        columnas_ortonormales.append(normalize(v))

    return transpose(columnas_ortonormales)


def matrix_to_str(matrix: list[list[float]]) -> str:
    """
    Convierte una matriz a texto para imprimirla de forma ordenada.
    """

    if len(matrix) == 0:
        return ""

    s = [[str(round(elemento, 10)) for elemento in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = "\t".join("{{:{}}}".format(x) for x in lens)
    table = [fmt.format(*row) for row in s]

    return "\n".join(table)