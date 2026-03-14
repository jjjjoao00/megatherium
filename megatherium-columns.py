print ("METODOLOGIA DE EXTRAÇÃO DE QUANTITATIVO DE FORMA PARA VIGAS DE CONCRETO ARMADO UTILIZANDO IFCOPENSHELL")

import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.shape
import ifcopenshell.util.element
import ifc5d
import math
import csv
import os 
import platform
from pathlib import Path

model = ifcopenshell.open('C:/Users/Dell/Desktop/DOCS/EXTRACAO-IFC/modelopilar2.ifc')

#PILARES
columns = model.by_type('IfcColumn')[0]
column_type = ifcopenshell.util.element.get_type(columns)
lado_x = []
lado_y = []
id_columns = []
total_lado_x = 0
total_lado_y = 0
total_faces = 0



#INICIALIZAÇÃO AUTOMATICA DO EXCEL
diretorio_script = os.path.dirname(os.path.abspath(__file__))
nome_arquivo = 'formas.csv'
caminho_final = os.path.join(diretorio_script, nome_arquivo)

#CALCULO DOS PILARES DO MODELO
#SELECIONA O PILAR NO MODELO PELO TIPO IFC 'IfcColumn'
for pilar in model.by_type ('IfcColumn', 1):
	#NOMEIA OS PILARES A PARTIR DA ESPECIFICAÇÃO TAG NO PROJETO
	print(pilar.Tag)

	#RETORNA A FORMA GEOMÉTRICA DOS PILARES NO MODELO
	settings = ifcopenshell.geom.settings()
	shape = ifcopenshell.geom.create_shape (settings, pilar)

	#RETORNA O VOLUME DE CADA PILAR
	volume = round(ifcopenshell.util.shape.get_volume(shape.geometry), 2)
	print (f'Volume de concreto : {volume} m3')

	#VERIFICAÇÃO DAS DIMENSÕES EM CADA EIXO
	#RETORNA A DIMENSÃO EM X
	facex = round(ifcopenshell.util.shape.get_x(shape.geometry), 2)
	print(f'face x: {facex:.2f}')

	#RETORNA A DIMENSÃO EM Y
	facey = round(ifcopenshell.util.shape.get_y(shape.geometry),2)
	print(f'face y: {facey:.2f}')

	#RETORNA A DIMENSÃO EM Z 
	facez = round (ifcopenshell.util.shape.get_z(shape.geometry), 2)
	print(f'face z: {facez:.2f}')

	#CALCULA A ÁREA DE SUPERFÍCIE EM DETERMINADO EIXO
	#EIXO Y
	area_y = round((ifcopenshell.util.shape.get_side_area(shape.geometry, 'Y', angle = 90.0)* 2),2)
	print (f'Area Y : {area_y:.2f} m2')

	#EIXO X
	area_x = round((ifcopenshell.util.shape.get_side_area(shape.geometry, 'X', angle = 90.0) *2),2)
	print (f'Area X : {area_x:.2f} m2')

	#CRIA A LISTA COM AS QUANTIDADES
	lado_x.append(area_x)
	lado_y.append(area_y)


	#SOMA OS VALORES DAS LISTAS DA QUANTIDADES E RETORNA A QUANTIDADE TOTAL EM M2
	total_x = sum(lado_x)
	total_y = sum(lado_y)

	total_faces = total_x + total_y

	#CRIA A LISTA DE ID DOS PILARES
	id_columns.append(pilar.Tag)



#CRIA O CSV
with open ('formas.csv', mode = 'w', newline = '', encoding ='utf-8') as arquivo:
	#CRIA O OBJETO QUE VAI SER O CSV
	escritor = csv.writer (arquivo, delimiter =';')

	#CABEÇALHO
	escritor.writerow (['ID', 'TOTAL X (M2)', 'TOTAL Y (M2)'])

	#NOMEIA OS PILARES A PARTIR DA TAG
	for desc, dim_x, dim_y in zip(id_columns, lado_x, lado_y):
		escritor.writerow([desc, f'{dim_x}', f'{dim_y}'])

		
	#LINHA EM BRANCO E TOTAL
	escritor.writerow([])
	escritor.writerow(['Total de formas para os pilares', ' ',f'{total_faces} M2'])	



print(f"Arquivo '{caminho_final}' criado!")

#PARA ABRIR AUTOMATICAMENTE
sistema = platform.system ()

if sistema == 'Windows':
	os.startfile(caminho_final)
elif sistema == 'Darwin': #mac
	os.system(f'open "{caminho_final}"')
else: #linux
	os.system(f'xdg-open"{caminho_final}"')