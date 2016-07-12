import csv

class MyCsv(object):
	_headerCsv = []
	_bodyCsv = []
	_hFile = ''

	def __init__(self, fileName)
		self._hFile = csv.reader(open(fileName,'rb'))
		self._generate()

	def _generate(self):
		for index, row in enumerate(self._hFile):
			self._bodyCsv.append(row)
		self._headerCsv = self._bodyCsv.pop(0)

	def results(self):
		return self._bodyCsv