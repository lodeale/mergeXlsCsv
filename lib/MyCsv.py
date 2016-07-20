import csv

class MyCsv(object):
	_bodyCsv = []
	_hFile = ''

	def __init__(self, fileName):
		self._hFile = csv.reader(open(fileName,'rb'))
		self._generate()

	def _generate(self):
		for index, row in enumerate(self._hFile):
			self._bodyCsv.append(row)

	def results(self,flag='body'):
		if flag == 'header':
			return self._bodyCsv.pop(0)
		return self._bodyCsv