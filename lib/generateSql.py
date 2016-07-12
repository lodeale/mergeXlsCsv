class GenerateSql(object):
	_insertStr = "INSERT INTO %s VALUES "
	_tableName = 'table.test'
	_insertList = []

	def __init__(self,tableName):
		self._tableName = tableName
		self._make()

	def _make(self,values):
		for row in values:
			start = '('
			end = ');'
			value = ''
			for field in row:
				value = value + str(field) + ','
			sqlComplet = self._insertStr + start + value[0:-1] + end
			self._insertList.append(sqlComplet)

	def results(self):
		return self._insertList