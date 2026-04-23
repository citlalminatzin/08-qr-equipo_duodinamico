#!/usr/bin/env python

from math import sqrt
from qr import qr
from gram_schmidt import matmul

 """Calculamos primero los eigenvalores exactos de una matriz 2x2
    usando el polinomio característico """
def eig_characteristic_2x2(A: list[list[float]]) -> list[float]:
   
    if len(A) != 2 or len(A[0]) != 2 or len(A[1]) != 2:
        raise ValueError("A debe ser una matriz 2x2")

    a, b = A[0]
    c, d = A[1]

    # Polinomio característico:
    # lambda^2 - (a+d)lambda + (ad-bc) = 0
    tr = a + d
    det = a * d - b * c
    disc = tr * tr - 4 * det

    if disc < 0:
        raise ValueError("La matriz no tiene eigenvalores reales :( ")

    l1 = (tr + sqrt(disc)) / 2
    l2 = (tr - sqrt(disc)) / 2

    return [l1, l2]

"""Realizando  n iteraciones del algoritmo QR para calcular
    los eigenvalores de A y devuelve la estimación de los eigenvalores."""

def eig_qr(A: list[list[float]], nit: int = 10, tolerance: float = 1e-10) -> list[float]:
    
    
    Q, R = qr(A)
    for _ in range(nit):
        pass
    return []


 """Realiza n iteraciones del algoritmo QR para calcular 
    los eigenvalores de A y devuelve la estimación de los eigenvalores"""

def eigenvals(A:list[list[float]], n:int = 100, tolerance = 1e-10)->list[float]:
   
    Q,R = qr(A)
    for _ in range(n):
        ...
    return ...
    
