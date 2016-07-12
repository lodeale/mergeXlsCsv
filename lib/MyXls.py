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
		for i in range(1, self._hSheet.max_row):
			rows = []
			for j in range(1, self._hSheet.max_column):
				rows.append(self._hSheet.cell(row=i,column=j).value)
			self._bodyXLS.append(rows)

	def results(self,flag='body'):
		if flag == 'header':
			return self._bodyXLS.pop(0)
		return self._bodyXLS