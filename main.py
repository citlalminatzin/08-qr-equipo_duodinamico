#!/usr/bin/env python

import collections
import numbers

from math import pi
from linear_solver import solve

from eigenvalues import eig_characteristic_2x2 
from eigenvalues import qr_simple

#EJERCICIO 1 
def main():
    A = [[5.0, -2.0],
         [-2.0, 8.0]]

    eigs = eig_characteristic_2x2(A)

    print("Matriz A:")
    for row in A:
        print(row)

    print("\nEigenvalores por polinomio característico:")
    print(eigs)


if __name__ == "__main__":
    main()

#Ejercicio 2 

def main():
    A = [
        [5.0, -2.0],
        [-2.0, 8.0]
    ]

    nit = 10

    Ak = qr_simple(A, nit)

    eigenvalores_aproximados = [Ak[i][i] for i in range(len(Ak))]

    print("\nResultado final:")
    print(f"Matriz A_{nit}:")
    for row in Ak:
        print(row)

    print("\nEigenvalores aproximados por el método QR simple:")
    print(eigenvalores_aproximados)

    print("\nEigenvalores exactos obtenidos en el ejercicio 1:")
    print([4.0, 9.0])


if __name__ == "__main__":
    main()


#EJERCICIO 3 












"""
# linspace obtenido de (https://code.activestate.com/recipes/579000/)
class linspace(collections.abc.Sequence):
    """linspace(start, stop, num) -> linspace object
    
    Return a virtual sequence of num numbers from start to stop (inclusive).
    
    If you need a half-open range, use linspace(start, stop, num+1)[:-1].
    """
    
    def __init__(self, start, stop, num):
        if not isinstance(num, numbers.Integral) or num <= 1:
            raise ValueError('num must be an integer > 1')
        self.start, self.stop, self.num = start, stop, num
        self.step = (stop-start)/(num-1)
    def __len__(self):
        return self.num
    def __getitem__(self, i):
        if isinstance(i, slice):
            return [self[x] for x in range(*i.indices(len(self)))]
        if i < 0:
            i = self.num + i
        if i >= self.num:
            raise IndexError('linspace object index out of range')
        if i == self.num-1:
            return self.stop
        return self.start + i*self.step
    def __repr__(self):
        return '{}({}, {}, {})'.format(type(self).__name__,
                                       self.start, self.stop, self.num)
    def __eq__(self, other):
        if not isinstance(other, linspace):
            return False
        return ((self.start, self.stop, self.num) ==
                (other.start, other.stop, other.num))
    def __ne__(self, other):
        return not self==other
    def __hash__(self):
        return hash((type(self), self.start, self.stop, self.num))  

def main():
    ...

if __name__ == "__main__":
    main()
"""