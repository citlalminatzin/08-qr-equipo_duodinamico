[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23625148)
# Práctica 8

¡Adentrémonos en el increíble mundo del álgebra lineal numérica! OwO

## Integrantes

- Garcia Chalche Julio Cesar 

## Uso e instalación



## Ejercicio 1. Cálculos con el polinomio característico

Sea la matriz


$$
A=
\begin{pmatrix}
5 & -2 \\
-2 & 8
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

## Ejercicio 2. El método QR simple

En este ejercicio se implementó el **método QR simple** para aproximar los eigenvalores de una matriz real, cuadrada y simétrica.

El método parte de una matriz inicial $$A_0 = A$$ y, en cada iteración, realiza la factorización QR de la matriz actual:

$$
A_k = Q_k R_k
$$

Después, se construye la siguiente matriz del proceso como:

$$
A_{k+1} = R_k Q_k
$$

Repitiendo este procedimiento varias veces, la matriz $$A_k$$ se va acercando a una matriz diagonal, y los valores de su diagonal se aproximan a los eigenvalores de la matriz original.

Para probar la implementación, se utilizó la matriz del ejercicio 1:

$$
A =
\begin{pmatrix}
5 & -2 \\
-2 & 8
\end{pmatrix}
$$

y se realizaron $$10$$ iteraciones del método QR.

El algoritmo implementado fue:

$$
A_0 = A
$$

$$
A_{k+1} = R_k Q_k
\quad \text{donde} \quad
A_k = Q_k R_k
$$

Al finalizar las iteraciones, se obtuvo una matriz $$A_{10}$$ aproximadamente diagonal. Por lo tanto, los valores en su diagonal son una aproximación de los eigenvalores de $$A$$.

Si denotamos por $$A_{10}$$ la matriz obtenida después de 10 iteraciones, entonces:

$$
\text{eigenvalores aproximados} \approx \operatorname{diag}(A_{10})
$$

En nuestro caso, la diagonal de la matriz resultante es aproximadamente:

$$
\lambda_1 \approx 9, \qquad \lambda_2 \approx 4
$$

Estos valores coinciden con los eigenvalores calculados en el ejercicio 1 por medio del polinomio característico:

$$
\lambda_1 = 4, \qquad \lambda_2 = 9
$$

### Conclusión

El método QR simple permitió aproximar correctamente los eigenvalores de la matriz

$$
A =
\begin{pmatrix}
5 & -2 \\
-2 & 8
\end{pmatrix}
$$

ya que, después de varias iteraciones, los elementos de la diagonal de $$A_k$$ convergen a los eigenvalores de la matriz original.