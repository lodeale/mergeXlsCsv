#!/usr/bin/python
import sys
from lib.MyCsv import MyCsv
from lib.generateSql import GenerateSql
from lib.MyXls import MyXls

if len(sys.argv) >= 2:
	fileName = sys.argv[1]
	fileNameXls = sys.argv[2]
	sheetName = sys.argv[3]

	res = MyCsv()
	#makeSQL = GenerateSql()
	xls = MyXls(fileNameXls,sheetName)

	res.get(fileName)
	xls.show()
	#makeSQL.make(res.bodyCsv)
else:
	print "Error: Debe pasar el nombre del archivo"

