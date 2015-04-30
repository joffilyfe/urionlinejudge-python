# -*- coding: utf-8 -*-
A, B, C = raw_input().split(" ")
A, B, C = float(A), float(B), float(C)
pi = 3.14159

print("TRIANGULO: %.3f" % ((A*C)/2))
print("CIRCULO: %.3f" % (pi * (C**2)))
print("TRAPEZIO: %.3f" % (((A+B) * C) / 2))
print("QUADRADO: %.3f" % (B*B))
print("RETANGULO: %.3f" % (A*B))
