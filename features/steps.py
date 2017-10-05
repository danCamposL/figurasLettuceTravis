# -*- coding: utf-8 -*-
# Eduardo Daniel Campos Loera
from lettuce import step, world
from areas import areas

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass

@step(u'Dado que ingreso el numero "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.areas = areas()
    world.areas.circulo(int(num1))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.areas.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

@step(u'Dado que ingreso el tamano "([^"]*)"')
def dado_que_ingreso_el_tamano_group1(step, num1):
    world.areas = areas()
    world.areas.cuadro(int(num1))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.areas.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

@step(u'Dado que ingreso la altura "([^"]*)" y base "([^"]*)"')
def dado_que_ingreso_la_altura_group1_y_base_group2(step, num1, num2):
    world.areas = areas()
    world.areas.rectangulo(int(num1), int(num2))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.areas.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

@step(u'Dado que ingreso la base mayor "([^"]*)" y base menor "([^"]*)" y altura de "([^"]*)"')
def dado_que_ingreso_la_base_mayor_group1_y_base_menor_group2_y_altura_de_group3(step, num1, num2, num3):
    world.areas = areas()
    world.areas.trapecio(int(num1), int(num2), int(num3))
@step(u'entonces obtengo el resultado "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
	obtenido = world.areas.obtener_resultado()
	assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)
