#!/usr/bin/python
# -*- encoding: utf-8 -*-
import sys, getopt
from termcolor import colored
import os


from lib.MyCsv import MyCsv
from lib.generateSql import GenerateSql
from lib.MyXls import MyXls
from lib.Merge import Merge

def main (argv):
	fileName1 = ''
	fileName2 = ''
	sheetName1 = ''
	sheetName2 = ''
	commonFields = ''
	fieldKeep = ''
	sqlFields = ''

	try:
		opts, args = getopt.getopt(argv,"h:'W1':'S1':'W2':'S2':'F':",["fileName1=","fileName2=", "sheetName=", "sheetName2=", "config="])
	except getopt.GetoptError:
		print 'app.py -W1 <inputfile1> -S1 <sheetName1> -W2 <inputfile2> -S2 <sheetName2> -F ->use ConfigFile "./conf/conf.conf"'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'app.py -F1 <inputfile1> -S1 <sheetName1> -F2 <inputfile2> -S2 <sheetName2> -F ->use ConfigFile "./conf/conf.conf"'
			sys.exit()
		elif opt =='-F':
			config=open('./conf/conf.conf')
			for row in config:
				if (row.startswith('PATH_FILE_1=') != 0):
					fileName1 = (row[12:]).rstrip('\n')
					print fileName2
				elif (row.startswith('SHEET_NAME_1=') != 0):
					sheetName1 = (row[13:]).rstrip('\n')
					print sheetName1
				elif (row.startswith('PATH_FILE_2=') != 0):
					fileName2 = (row[12:]).rstrip('\n')
					print fileName2
				elif (row.startswith('SHEET_NAME_2=') != 0):
					sheetName2 = (row[13:]).rstrip('\n')
					print sheetName2
				elif (row.startswith('COMMON_FIELDS=') != 0):
					row = (row[15:(len(row)-1)]).rstrip('\n')
					commonFields=row.split(',')
				elif (row.startswith('FIELDS_TO_KEEP=') != 0):
					row = (row[15:(len(row)-1)]).rstrip('\n')
					fieldKeep=row.split(',')
				elif (row.startswith('SQL_FIELDS=') != 0):
					row = (row[12:(len(row)-1)]).rstrip('\n')
					sqlFields=row.split(',')
			break
		elif opt in ("-W1", "--fileName1"):
			fileName1 = arg
		elif opt in ("-W2", "--fileName2"):
			fileName2 = arg
		elif opt in ("-S1", "--sheetName"):
			sheetName2 = arg
		elif opt in ("-S2", "--sheetName"):
			sheetName1 = arg

	cabecera()

	format1 = fileName1.split('.')[-1]
	format2 = fileName2.split('.')[-1]
	arrayFile1 = []
	arrayFile2 = []
	print "\n[+] Procesando File 1"
	try:
		if ( format1.lower() == "xls" or format1.lower() == "xlsx"):
			arrayFile1 = MyXls(fileName1,sheetName1)
		elif ( format1.lower() == "csv" ):
			arrayFile1 = MyCsv(fileName1)
		else:
			print "\n No se reconoce el formato del archivo 1."
	except Exception, e:
		print "\nError Archivo 1: ", e

	print "\n[+] Procesando File 2"
	try:
		if ( format2.lower() == "xls" or format2.lower() == "xlsx"):
			arrayFile2 = MyXls(fileName2,sheetName2)
		elif ( format2.lower() == "csv"):
			arrayFile2 = MyCsv(fileName2)
		else:
			print "\n No se reconoce el formato del archivo 2."
	except Exception, e:
		print "\nError Archivo 2: ", e

	if ( arrayFile1 ):
		if ( arrayFile2 ):
			print "\n[+] Generando Merge con ambos archivos"
			merge = Merge(arrayFile1.results(), arrayFile2.results(), commonFields, fieldKeep)
			merge = merge.results()
		else:
			merge = arrayFile1.results()
	else:
		print "\n[+]No agrego ningún archivo."

	print "\n[+] Generando SQL"
	sql = GenerateSql("empresas_brasil.linea_credito_empresas_brasil",sqlFields,merge)

	print "\n[+] Creando archivo /tmp/DBChange.sql"
	if ( os.path.exists('/tmp/DBChange.sql') ):
		os.remove('/tmp/DBChange.sql')
	fileO = open('/tmp/DBChange.sql','a')
	
	print "\n[+] Escribiendo los inserts"
	for row in sql.results():
		fileO.write(str(row) + "\n")
	fileO.close()
	print "\n[+] Fin de la creación."

def cabecera():
	print """ \x1b[32m\n\n

		################
		# SamanaBeeLeo #
		################
		\n\n
	 
	________$$$$$$$$$$________ 
	_____d$$$$$$$$$$$$$b______ 
	_____$$$$$$$$$$$$$$$$_____ 
	____4$$$$$$$$$$$$$$$$F____ 
	____4$$$$$$$$$$$$$$$$F____ 
	____$$$$"_"$$$$"_"$$$$_____ 
	_____$$F___4$$F___4$$_____ 
	_____´$F___4$$F___4$"_____
	______$$___$$$$___$P______ 
	______4$$$$$"^$$$$$%_____
	_______$$$$F__4$$$$_______ 
	________"$$$ee$$$"________
	________._*$$$$F4_________
	_________$_____.$_________
	_________"$$$$$$"_________
	__________^$$$$___________ 
	_4$$c_______""_______.$$r_ 
	_^$$$b____\x1b[0m\x1b[31mSamana\x1b[0m\x1b[32m____e$$$"_
	_d$$$$$e__________z$$$$$b_ 
	4$$$*$$$$$c____.$$$$$*$$$r 
	_""____^*$$$be$$$*"____^"_ 
	_\x1b[0m\x1b[31mRomeo\x1b[0m\x1b[32m____"$$$$"___\x1b[0m\x1b[31mDelta\x1b[0m\x1b[32m__
	________.d$$P$$$b_________ 
	_______d$$P___^$$$b_______ 
	___.ed$$$"______"$$$be.___ 
	_$$$$$$P___\x1b[0m\x1b[31mBEE\x1b[0m\x1b[32m____*$$$$$$_ 
	4$$$$$P____\x1b[0m\x1b[31mLEO\x1b[0m\x1b[32m____$$$$$$" 
	_"*$$$"____________^$$P___
	____""______________^"____\x1b[0m
	"""

if __name__ == "__main__":
	  
	main(sys.argv[1:])