import openpyxl, pprint

class MyXls(object):
	headerXLS = []
	bodyXLS = []
	hBook = ''
	hSheet = ''
	
	def __init__(self, fileName, sheetName):
		self.hBook = openpyxl.load_workbook(fileName)
		self.hSheet = self.hBook.get_sheet_by_name(sheetName)
		self._generate()
	
	def _generate(self):
		for row in range(2, self.hSheet.max_row + 1):
			cnpj = str(self.hSheet['M' + str(row)].value)
			creditLine = int(self.hSheet['O' + str(row)].value)
			self.bodyXLS.append([cnpj,creditLine])

	def results(self):
		return self.bodyXSL

	def show(self):
		data = pprint.pformat(self.bodyXLS)
		print data