from saludo import saludar as sa
from despedidas import despedida as de
v = True
while v:
	n = int(input('*-*-*- BIENVENIDO AL PROGRAMA QUE TE SALUDA, DESPIDE Y DESEA SUERTE -*-*-*\n Que quieres hacer?\n1)SALUDAR\n2)DESPEDIR\n0)SALIR\n'))
	if n == 0:
		v = False
	elif n == 1:
		v = False
		sa()
	elif n == 2:
		v = False
		de()


