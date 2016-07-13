#!/usr/bin/python
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
	
	cvs = MyCsv(fileName1)
	xls = MyXls(fileName2,sheetName)
	merge = Merge(cvs.results(), xls.results(), ['ECREDIT_LINE_ID','CD_CTA_CORRENTE'],['CNPJ','ECREDIT_LINE_ID','CURRENCY','CAPPING_AMOUNT','RUNNING_AMOUNT','STATUS'])
	sql = GenerateSql("empresa.test",merge.results())
	for row in sql.results():
		print row,"\n\n"
	#print cvs.results()
	#print xls.results()


if __name__ == "__main__":
   main(sys.argv[1:])