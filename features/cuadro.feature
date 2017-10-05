Feature: Evaluar area de un cuadro
	Como usuario del programa
	deseo calcular el area de un cuadro
	para obtener el resultado correcto

	Scenario: Lado de 8
		Dado que ingreso el tamano "8"
		cuando realizo la operacion
		entonces obtengo el resultado "64"

  Scenario: Lado de 15
		Dado que ingreso el tamano "15"
		cuando realizo la operacion
		entonces obtengo el resultado "225"
