import sympy as sym

x = sym.Symbol('x')

func = input("Function: ")

print(sym.Derivative(func, x, evaluate=True))
