#!/usr/bin/env python

from math import sqrt
from qr import qr
from gram_schmidt import matmul, matrix_to_str

""" Calculamos primero los eigenvalores exactos de una matriz 2x2
    usando el polinomio característico .-. """
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
   

#EJERCICIO 2 

""" realiza nit iteraciones del método QR simple
Recibe:
        A: matriz cuadrada y simétrica.
        nit: número de iteraciones.
 Devuelve:
        La matriz A_k después de nit iteraciones.
 demás  imprime cada iteración realizada   """

def qr_simple(A: list[list[float]], nit: int = 10) -> list[list[float]]:
    

    if len(A) == 0 or any(len(row) != len(A) for row in A):
        raise ValueError("A debe ser una matriz cuadrada :| ")

    Ak = [row[:] for row in A]

    print("Matriz inicial A_0:")
    print(matrix_to_str(Ak))

    for k in range(nit):
        Q, R = qr(Ak)
        Ak = matmul(R, Q)

        print(f"\nIteración {k + 1}:")
        print(f"Matriz A_{k + 1}:")
        print(matrix_to_str(Ak))

        diagonal = [Ak[i][i] for i in range(len(Ak))]
        print(f"Diagonal de A_{k + 1}: {diagonal}")

    return Ak


def eigenvals_qr_simple(A: list[list[float]], nit: int = 10) -> list[float]:
    
    #Calcula una aproximación de los eigenvalores usando el método QR simple 

    Ak = qr_simple(A, nit)
    eigenvalores = [Ak[i][i] for i in range(len(Ak))]

    return eigenvalores


#EJERCICIO 3, ahora si xD 


"""verifica si todos los elementos fuera de la diagonal
    tienen valor absoluto menor que epsilon >_<  """

def fuera_diagonal_menor_que_epsilon(A: list[list[float]], epsilon: float) -> bool:
   
    n = len(A)

    for i in range(n):
        for j in range(n):
            if i != j and abs(A[i][j]) >= epsilon:
                return False

    return True

""" El método QR con tolerancia, como se pide en el ejerccio
 Recibe:
        A: matriz cuadrada y simétrica
        epsilon: tolerancia deseada
        max_iter: número máximo de iteraciones
Devuelve:
        La matriz A_k cuando los valores fuera de la diagonal
        son menores que epsilon, o cuando se alcanza max_iter
Y además imprime las iteraciones realizadas """
def qr_metodo(A: list[list[float]], epsilon: float = 1e-10, max_iter: int = 1000) -> list[list[float]]:

    if len(A) == 0 or any(len(row) != len(A) for row in A):
        raise ValueError("A debe ser una matriz cuadrada")

    Ak = [row[:] for row in A]

    print("Matriz inicial A_0:")
    print(matrix_to_str(Ak))

    for k in range(max_iter):
        Q, R = qr(Ak)
        Ak = matmul(R, Q)

        print(f"\nIteración {k + 1}:")
        print(f"Matriz A_{k + 1}:")
        print(matrix_to_str(Ak))

        diagonal = [Ak[i][i] for i in range(len(Ak))]
        print(f"Diagonal de A_{k + 1}: {diagonal}")

        if fuera_diagonal_menor_que_epsilon(Ak, epsilon):
            print(f"\nEl método alcanzó la tolerancia epsilon = {epsilon}")
            print(f"Número de iteraciones realizadas: {k + 1}")
            return Ak

    print(f"\nNo se alcanzó la tolerancia epsilon = {epsilon}")
    print(f"Se llegó al número máximo de iteraciones: {max_iter}")

    return Ak


def eigenvals_qr(A: list[list[float]], epsilon: float = 1e-10, max_iter: int = 1000) -> list[float]:
    
    #Calcula una aproximación de los eigenvalores usando el método QR con tolerancia 

    Ak = qr_metodo(A, epsilon, max_iter)
    eigenvalores = [Ak[i][i] for i in range(len(Ak))]

    return eigenvalores