from saludo import saludar as sa
from despedidas import despedida as de
from suerte import suerte as su
v = True
while v:
	n = int(input('*-*-*- BIENVENIDO AL PROGRAMA QUE TE SALUDA, DESPIDE Y DESEA SUERTE -*-*-*\n Que quieres hacer?\n1)SALUDAR\n2)DESPEDIR\n3)DESEAR SUERTE\n0)SALIR\n'))
	if n == 0:
		v = False
	elif n == 1:
		v = False
		sa()
	elif n == 2:
		v = False
		de()
	elif n == 3:
		v = False
		su()


