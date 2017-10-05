Feature: Evaluar area de un trapecio
	Como usuario del programa
	deseo calcular el area de un trapecio
	para obtener el resultado correcto

	Scenario: Base mayor de 8, base menor de 10, altura de 8
		Dado que ingreso la base mayor "8" y base menor "10" y altura de "8"
		cuando realizo la operacion
		entonces obtengo el resultado "72"

  Scenario: Base mayor de 18, base menor de 100, altura de 15
		Dado que ingreso la base mayor "18" y base menor "100" y altura de "15"
		cuando realizo la operacion
		entonces obtengo el resultado "885"
