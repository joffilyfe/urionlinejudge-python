# -*- coding: utf-8 -*-
P1 = raw_input().split(" ")
P2 = raw_input().split(" ")


resultado = (int(P1[1]) * float(P1[2])) + ( int(P2[1]) * float(P2[2]) )
print("VALOR A PAGAR: R$ %.2f" % float(resultado))