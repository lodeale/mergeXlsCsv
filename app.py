#!/usr/bin/python
import sys, getopt

from lib.MyCsv import MyCsv
from lib.generateSql import GenerateSql
from lib.MyXls import MyXls

fileName1 = ''
fileName2 = ''
sheetName = ''

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
	# print 'File Name 1 => ', fileName1
	# print 'File Name 2 => ', fileName2
	# print 'Sheet Name => ', sheetName
	

	res = MyCsv(fileName1)
	xls = MyXls(fileName2,sheetName)
	print "===================================="
	print "CSV"
	print "===================================="
	print res.results()
	print "===================================="
	print "XLSX"
	print "===================================="
	print xls.results()


if __name__ == "__main__":
   main(sys.argv[1:])


# if len(sys.argv) >= 2:
# 	print 'File Name 1 => ', fileName1
# 	print 'File Name 2 => ', fileName2
# 	print 'Sheet Name => ', sheetName 

# 	# fileName = sys.argv[1]
# 	# fileNameXls = sys.argv[2]
# 	# sheetName = sys.argv[3]

# 	res = MyCsv(fileName1)
# 	#makeSQL = GenerateSql()
# 	xls = MyXls(fileName2,sheetName)

# 	res.get(fileName1)
# 	xls.show()
# 	#makeSQL.make(res.bodyCsv)
# else:
# 	print "Error: Debe pasar el nombre del archivo"

