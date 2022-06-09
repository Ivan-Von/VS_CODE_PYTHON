from scipy import integrate
import sympy
def f(x):
    return (x*sympy.exp(x))/((1+x) ** 2)
w, err = integrate.quad(f,0,1)
print(w)