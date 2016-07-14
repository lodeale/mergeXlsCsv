#!/usr/bin/python
# -*- encoding: utf-8 -*-
import sys, getopt

from lib.MyCsv import MyCsv
from lib.generateSql import GenerateSql
from lib.MyXls import MyXls
from lib.Merge import Merge

def main (argv):
	fileName1 = ''
	fileName2 = ''
	sheetName = ''
	try:
		opts, args = getopt.getopt(argv,"ha:b:s:",["fileName1=","fileName2=", "sheetName="])
	except getopt.GetoptError:
		print 'app.py -a <inputfile1> -b <inputfile2> -s <sheetName>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'app.py -f1 <inputfile1> -f2 <inputfile2> -s <sheetName>'
			sys.exit()
		elif opt in ("-a", "--fileName1"):
			fileName1 = arg
		elif opt in ("-b", "--fileName2"):
			fileName2 = arg
		elif opt in ("-s", "--sheetName"):
			sheetName = arg
	
	print "\n[+] Procesando File 1"
	cvs = MyCsv(fileName1)
	print "\n[+] Procesando File 2"
	xls = MyXls(fileName2,sheetName)
	print "\n[+] Generando Merge con ambos archivos"
	merge = Merge(cvs.results(), xls.results(), ['ECREDIT_LINE_ID','CD_CTA_CORRENTE'],['CNPJ','ECREDIT_LINE_ID','CURRENCY','CAPPING_AMOUNT','RUNNING_AMOUNT','STATUS'])
	print "\n[+] Generando SQL"
	sql = GenerateSql("empresa.test",merge.results())
	print "\n[+] Creando archivo /tmp/DBChange.sql"
	fileO = open('/tmp/DBChange.sql','a')
	for row in sql.results():
		fileO.write(str(row) + "\n")
	fileO.close()
	print "\n[+] Fin de la creación."

	print "Cantidad registros: ", xls.counts()
	print "Cantidad de errores: ", xls.errorsCount()



if __name__ == "__main__":
	print """\n\n
		################
		#  SamanaBee   #
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
	_^$$$b____Samana____e$$$"_
	_d$$$$$e__________z$$$$$b_ 
	4$$$*$$$$$c____.$$$$$*$$$r 
	_""____^*$$$be$$$*"____^"_ 
	_Romeo____"$$$$"___Delta__
	________.d$$P$$$b_________ 
	_______d$$P___^$$$b_______ 
	___.ed$$$"______"$$$be.___ 
	_$$$$$$P___BEE____*$$$$$$_ 
	4$$$$$P____________$$$$$$" 
	_"*$$$"____________^$$P___
	____""______________^"____
	"""
   
	main(sys.argv[1:])