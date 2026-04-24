#!/usr/bin/env python

from eigenvalues import eig_characteristic_2x2 
from eigenvalues import qr_simple
from eigenvalues import qr_metodo

   #EJERCICIO 1 
def main():
    A = [[5.0, -2.0],
         [-2.0, 8.0]]

    print("=" * 50)
    print("EJERCICIO 1: Polinomio característico")
    print("=" * 50)
    eigs = eig_characteristic_2x2(A)

    print("Matriz A:")
    for row in A:
        print(row)

    print("\nEigenvalores por polinomio característico:")
    print(eigs)


    #Ejercicio 2 
    print("\n" + "=" * 50)
    print("EJERCICIO 2: Método QR simple")
    print("=" * 50)

    nit = 10
    Ak_simple = qr_simple(A, nit)
    eigenvalores_aproximados = [Ak_simple[i][i] for i in range(len(Ak_simple))]

    print("\nResultado final:")
    print(f"Matriz A_{nit}:")
    for row in Ak_simple:
        print(row)

    print("\nEigenvalores aproximados por el método QR simple:")
    print(eigenvalores_aproximados)

    print("\nEigenvalores exactos obtenidos en el ejercicio 1:")
    print([4.0, 9.0])


    #EJERCICIO 3 

    print("\n" + "=" * 50)
    print("EJERCICIO 3: Método QR con tolerancia")
    print("=" * 50)

    epsilon = 1e-10
    max_iter = 1000

    Ak = qr_metodo(A, epsilon, max_iter)

    eigenvalores_aproximados = [Ak[i][i] for i in range(len(Ak))]

    print("\nResultado final:")
    print("Matriz final A_k:")
    for row in Ak:
        print(row)

    print("\nEigenvalores aproximados por el método QR:")
    print(eigenvalores_aproximados)

    print("\nEigenvalores exactos obtenidos en el ejercicio 1:")
    print([4.0, 9.0])


if __name__ == "__main__":
    main() fix