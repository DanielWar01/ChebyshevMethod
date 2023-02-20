import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
from math import *

def aproxFunction(f, n, a, b, x):
    c_i = 0
    c_k = []
    g_x = 0
    for i in range(n+1):
        for c in range(n+1):
            if (i == 0):
                c_i = c_i+(1/(n+1))*f(cos(pi*((2*c+1)/(2*n+2))))
            else:
                c_i = c_i+(2/(n+1))*f(cos(pi*((2*c+1)/(2*n+2))))*cos(i*pi*((2*c+1)/(2*n+2)))
            if c == 3:
                c_k.append(c_i)
                c_i = 0
        g_x = g_x+c_k[i]*chebyshev(i,x)
    return g_x

def chebyshev(n, x):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return 2*x*chebyshev(n-1, x)-chebyshev(n-2,x)

x = sp.symbols('x')
f = sp.simplify(chebyshev(3,x))
function = "exp(x)"
function = sp.lambdify(x, function)
print(f"El polinomio de chebyshev es: {sp.expand(f)}")
print(sp.simplify(aproxFunction(function, 3, -1, 1, x)))
g = sp.simplify(aproxFunction(function, 3, -1, 1, x))
g = sp.lambdify(x, g)
points = np.linspace(-3,3, 100)
plt.title(f'Funcion')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axhline(0, color='k')
plt.axvline(0, color='k')
plt.grid(True)
plt.plot(points, function(points))
plt.plot(points, g(points))
plt.show()
