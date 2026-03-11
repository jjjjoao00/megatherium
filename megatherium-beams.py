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

#print(ifcopenshell.version)

model = ifcopenshell.open('C:/Users/Dell/Desktop/DOCS/EXTRACAO-IFC/modeloviga3.ifc')

#print(model.schema)

#print(model.by_guid('3BQMEDNX51sv31xQw3nvH$'))

beams = model.by_type('IfcBeam')[0]
beam_type = ifcopenshell.util.element.get_type(beams)
psets = ifcopenshell.util.element.get_psets(beams)

pset_and_qtos = ifcopenshell.util.element.get_pset(beams, 'Pset_BeamCommon')

tampa_z = []
lateral_y = []
base_x = []

total_tampa_z = 0
total_base_x = 0
total_lateral_y = 0

total_faces = 0

diretorio_script = os.path.dirname(os.path.abspath(__file__))
nome_arquivo = 'formas.csv'
caminho_final = os.path.join(diretorio_script, nome_arquivo)

#CALCULO DAS VIGAS DO MODELO
#SELECIONA A VIGA NO MODELO PELO TIPO DELA "IfcBeam"
for viga in model.by_type('IfcBeam', 1):
	#NOMEIA CADA VIGA A PARTIR DA ESPECIFIAÇÃO TAG NO PROJETO
	print(viga.Tag)
	
	#ESPECIFICA UMA VIGA PARA ESTUDO A PARTIR DO GLOBALID
	#if viga.GlobalId == '2H1oP3Na99ygsjqS8bEEXR':
		#RETORNA A FORMA GEOMÉTRICA DA VIGA ESTUDADA
	settings = ifcopenshell.geom.settings()
	shape = ifcopenshell.geom.create_shape(settings, viga)

		#RETORNA O VOLUME DA VIGA
	volume = round (ifcopenshell.util.shape.get_volume(shape.geometry), 2)
	print (f'Volume de concreto: {volume} m3')

		#VERIFICAÇÃO DAS MEDIDAS EM CADA EIXO

		#RETORNA A DIMENSÃO EM X
	facesx = round (ifcopenshell.util.shape.get_x(shape.geometry) ,2)
	print (f'face x: {facesx:.2f}' )

		#RETORNA A DIMENSÃO EM Y
	facesy = round (ifcopenshell.util.shape.get_y(shape.geometry), 2)
	print(f'face y: {facesy:.2f}')

		#RETORNA A DIMENSÃO EM Z
	facesz = round (ifcopenshell.util.shape.get_z(shape.geometry), 2)
	print (f'face z: {facesz:.2f}')

		#CALCULA A AREA DA SUPERFICIE EM DETERMINADO EIXO
		#AREA DE SUPERFICIE DA TAMPA (PONTAS DA VIGA)
	area_tampa= round ((ifcopenshell.util.shape.get_side_area(shape.geometry, 'Z', angle = 90.0)*2) ,2)
	print (f'Area da tampa (Z da tampa) : {area_tampa:.2f} m2')

		#CALCULA A AREA DE SUPERFICIE LATERAL
	area_lateral= round ((ifcopenshell.util.shape.get_side_area(shape.geometry, 'X', angle = 90.0)*2), 2)
	print (f'Area lateral (Y da face): {area_lateral:.2f} m2')

		#CALCULA A AREA DE SUPERFICIE BASE
	area_base= round (ifcopenshell.util.shape.get_side_area(shape.geometry, 'Y', angle = 90.0) ,2)
	print (f'Area da base (X da base): {area_base:.2f} m2')


		#CRIA UMA LISTA COM AS QUANTIDADES CALCULADAS EM M2
	tampa_z.append(area_tampa)
	base_x.append(area_base)
	lateral_y.append(area_lateral)

		#SOMA OS VALORES DAS LISTAS DAS QUANTIDADES E RETORNA A QUANTIDADE TOTAL EM M2
	total_tampa_z = sum(tampa_z)
	total_base_x = sum(base_x)
	total_lateral_y = sum(lateral_y)

	total_faces = total_tampa_z + total_base_x + total_lateral_y



#CRIA O CSV
with open ('formas.csv', mode = 'w', newline = '', encoding ='utf-8') as arquivo:
	#CRIA O OBJETO QUE VAI SER O CSV
	escritor = csv.writer (arquivo, delimiter =';')

	#CABEÇALHO
	escritor.writerow (['NOME', 'TOTAL M2'])


	#LINHA EM BRANCO E TOTAL
	escritor.writerow([])
	escritor.writerow(['Total de formas para as vigas', f'{total_faces} M2'])	



print(f"Arquivo '{caminho_final}' criado!")

#PARA ABRIR AUTOMATICAMENTE
sistema = platform.system ()

if sistema == 'Windows':
	os.startfile(caminho_final)
elif sistema == 'Darwin': #mac
	os.system(f'open "{caminho_final}"')
else: #linux
	os.system(f'xdg-open"{caminho_final}"')


















#print (tampa_z)
#print (base_y)
#print (lateral_x)

#print(f'Total de material para formas na área da tampa: {total_tampa_z:.2f} m2')
#print(f'Total de material para formas na área da base: {total_base_x:.2f} m2')
#print(f'Total de material para formas na área das faces laterais: {total_lateral_y:.2f} m2')

#print(total_faces)




#TODO
#EXPORTAR EM CSV



#print (beams.GlobalId)
#print (beams.Name)


#conta quantos tipos tem no arquivo
print (f'Total de trechos', len(beam_type))

#print (ifcopenshell.util.element.get_psets(beams))
#print(beams.IsDefinedBy)

#print(beams)

