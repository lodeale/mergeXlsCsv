import openpyxl

class MyXls(object):
	_bodyXLS = []
	_hBook = ''
	_hSheet = ''
	
	def __init__(self, fileName, sheetName):
		self._hBook = openpyxl.load_workbook(fileName)
		self._hSheet = self._hBook.get_sheet_by_name(sheetName)
		self._generate()
	
	def _generate(self):
		for row in range(2, self._hSheet.max_row + 1):
			cnpj = str(self._hSheet['M' + str(row)].value)
			creditLine = int(self._hSheet['O' + str(row)].value)
			self._bodyXLS.append([cnpj,creditLine])

	def results(self):
		return self.bodyXSL