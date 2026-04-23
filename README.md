[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23625148)
# Práctica 8

¡Adentrémonos en el increíble mundo del álgebra lineal numérica! OwO

## Integrantes

- Garcia Chalche Julio Cesar 

## Uso e instalación



## Ejercicio 1. Cálculos con el polinomio característico

Sea la matriz

$$

A = 
    \begin{pmatrix} 5 & -2 
    \\ -2 & 8 
    \end{pmatrix}

$$

Para encontrar sus eigenvalores, calculamos el polinomio característico resolviendo:


$$
\det(A-\lambda I)=0
$$

Primero obtenemos:

$$
A-\lambda I=
\begin{pmatrix}
5-\lambda & -2 \\
-2 & 8-\lambda
\end{pmatrix}
$$

Ahora calculamos su determinante:

$$
\det(A-\lambda I)=
\begin{vmatrix}
5-\lambda & -2 \\
-2 & 8-\lambda
\end{vmatrix}
$$

$$
\det(A-\lambda I)=(5-\lambda)(8-\lambda)-(-2)(-2)
$$

$$
=(5-\lambda)(8-\lambda)-4
$$

Desarrollando el producto:

$$
(5-\lambda)(8-\lambda)=40-13\lambda+\lambda^2
$$

Sustituyendo:

$$
\det(A-\lambda I)=40-13\lambda+\lambda^2-4
$$

$$
=\lambda^2-13\lambda+36
$$

Por lo tanto, el polinomio característico es:

$$
p(\lambda)=\lambda^2-13\lambda+36
$$

Ahora resolvemos la ecuación:

$$
\lambda^2-13\lambda+36=0
$$

Factorizando:

$$
(\lambda-4)(\lambda-9)=0
$$

De aquí se obtiene que los eigenvalores son:

$$
\lambda_1=4
\qquad
\lambda_2=9
$$

### Conclusión

Los eigenvalores de la matriz

$$
A=
\begin{pmatrix}
5 & -2 \\
-2 & 8
\end{pmatrix}
$$

son:

$$
\boxed{4 \text{ y } 9}
$$
