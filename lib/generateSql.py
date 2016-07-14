class GenerateSql(object):
	_insertStr = "INSERT INTO "
	_insertStrValues = " VALUES "
	_tableName = 'table.test'
	_insertList = []

	def __init__(self,tableName,arrayValues):
		self._tableName = tableName
		self._make(arrayValues)

	def _make(self,values):
		for row in values:
			start = '('
			end = ');'
			value = ''
			for field in row:
				value = value + "'" + str(field) + "'" + ","
			sqlComplet = self._insertStr + self._tableName + self._insertStrValues + start + value[0:-1] + end
			self._insertList.append(sqlComplet)

	def results(self):
		return self._insertList