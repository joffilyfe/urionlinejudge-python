# -*- coding: utf-8 -*-
a, b, c = raw_input().split(" ")
a, b, c = int(a), int(b), int(c)
p = (a+b+(abs(a-b))) / 2
s = (b+c+(abs(b-c))) / 2

if (p > s):
  maior = p
else:
  maior = s
  
print("%d eh o maior" % maior)