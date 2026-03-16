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
import re

#instancia o modelo
model = ifcopenshell.open('C:/Users/Dell/Desktop/DOCS/EXTRACAO-IFC/modeloviga3.ifc')

#VIGAS
beams = model.by_type('IfcBeam')[0]
beam_type = ifcopenshell.util.element.get_type(beams)
tampa_z = []
lateral_x = []
base_y = []
id_beams = []
id_beams_ordenado = sorted(id_beams, key=lambda x: int(re.search(r'\d+', x ).group()))
total_tampa_z = 0
total_base_y = 0
total_lateral_x = 0
total_faces = 0

dados = []

#INICIALIZAÇÃO AUTOMATICA DO EXCEL
diretorio_script = os.path.dirname(os.path.abspath(__file__))
nome_arquivo = 'formas.csv'
caminho_final = os.path.join(diretorio_script, nome_arquivo)

#CALCULO DAS VIGAS DO MODELO
#SELECIONA A VIGA NO MODELO PELO TIPO DELA "IfcBeam"
for viga in model.by_type('IfcBeam', 1):
	#NOMEIA CADA VIGA A PARTIR DA ESPECIFIAÇÃO TAG NO PROJETO
	print(viga.Tag)

	#RETORNA A FORMA GEOMÉTRICA DA VIGA ESTUDADA
	settings = ifcopenshell.geom.settings()
	shape = ifcopenshell.geom.create_shape(settings, viga)

		#RETORNA O VOLUME DE CADA VIGA
	volume = round (ifcopenshell.util.shape.get_volume(shape.geometry), 2)
	print (f'Volume de concreto: {volume} m3')

		#VERIFICAÇÃO DAS MEDIDAS EM CADA EIXO

		#RETORNA A DIMENSÃO EM X
	facesy = round (ifcopenshell.util.shape.get_x(shape.geometry) ,2)
	print (f'face x: {facesy:.2f}' )

		#RETORNA A DIMENSÃO EM Y
	facesx = round (ifcopenshell.util.shape.get_y(shape.geometry), 2)
	print(f'face y: {facesx:.2f}')

		#RETORNA A DIMENSÃO EM Z
	facesz = round (ifcopenshell.util.shape.get_z(shape.geometry), 2)
	print (f'face z: {facesz:.2f}')

		#CALCULA A AREA DA SUPERFICIE EM DETERMINADO EIXO
		#AREA DE SUPERFICIE DA TAMPA (PONTAS DA VIGA)
	area_tampa= round ((ifcopenshell.util.shape.get_side_area(shape.geometry, 'Z', angle = 90.0)*2) ,2)
	print (f'Area da tampa (Z da tampa) : {area_tampa:.2f} m2')

		#CALCULA A AREA DE SUPERFICIE LATERAL
	area_lateral= round ((ifcopenshell.util.shape.get_side_area(shape.geometry, 'Y', angle = 90.0)), 2)
	print (f'Area da base (Y da base): {area_lateral:.2f} m2')

		#CALCULA A AREA DE SUPERFICIE BASE
	area_base= round ((ifcopenshell.util.shape.get_side_area(shape.geometry, 'X', angle = 90.0)*2) ,2)
	print (f'Area da lateral (X da face): {area_base:.2f} m2')

		#CRIA UMA LISTA COM AS QUANTIDADES CALCULADAS EM M2
	tampa_z.append(area_tampa)
	base_y.append(area_base)
	lateral_x.append(area_lateral)

		#SOMA OS VALORES DAS LISTAS DAS QUANTIDADES E RETORNA A QUANTIDADE TOTAL EM M2
	total_tampa_z = sum(tampa_z)
	total_base_y = sum(base_y)
	total_lateral_x = sum(lateral_x)

	total_faces = total_tampa_z + total_base_y + total_lateral_x

	#CRIA A LISTA DE ID DAS VIGAS
	id_beams.append(viga.Tag)





# Adicione isso para ver como os dados estão chegando no Python
#print(f"DEBUG - Dados da linha: {lateral_x}"f'{base_y}'f'{tampa_z}')
print(id_beams)


#CRIA O CSV
with open ('formas.csv', mode = 'w', newline = '', encoding ='utf-8') as arquivo:
	#CRIA O OBJETO QUE VAI SER O CSV
	escritor = csv.writer (arquivo, delimiter =';')
	leitor = csv.DictReader (arquivo)
	coluna_alvo = 'ID'

	#CABEÇALHO
	escritor.writerow (['ID', 'TOTAL X (M2)', 'TOTAL Y (M2)', 'TOTAL Z (M2)'])


	id_beams_ordenados = sorted(id_beams, key=lambda x: int(re.search(r'\d+',x).group()))

	#NOMEIA AS VIGAS A PARTIR DA TAG
	for desc, dim_x, dim_y, dim_z in zip (id_beams_ordenados, lateral_x, base_y, tampa_z):
		escritor.writerow([desc, f'{dim_x}', f'{dim_y}', f'{dim_z}'])


	#LINHA EM BRANCO E TOTAL
	escritor.writerow([])
	escritor.writerow(['Total de formas para as vigas', ' ',f'{total_faces} M2'])	

	


print(f"Arquivo '{caminho_final}' criado!")

#PARA ABRIR AUTOMATICAMENTE
sistema = platform.system ()

if sistema == 'Windows':
	os.startfile(caminho_final)
elif sistema == 'Darwin': #mac
	os.system(f'open "{caminho_final}"')
else: #linux
	os.system(f'xdg-open"{caminho_final}"')



#TODO#
#CRIAR UMA INTERFACE SIMPLES
#PASSAR PARA A VERSÃO FINAL


#VERSAO FINAL
# Leitura e parse de arquivos IFC (IFC2X3 e IFC4) ok
#Identificação automática de pilares e vigas no modelo ok
#Cálculo preciso da área de fôrma para cada elemento ok
#Relatórios detalhados em formato CSV e Excel OK
#Agrupamento por pavimento/tipo de elemento 




