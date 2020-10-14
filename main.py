from saludo import saludar as sa
v = True
while v:
	n = int(input('*******Bienvenido al programa que te saluda*******\n Que quieres hacer?\n1)SALUDAR\n0)SALIR\n'))
	if n == 0:
		v = False
	if n == 1:
		v = False
		sa()


