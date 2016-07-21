class GenerateSql(object):
	_insertStr = "INSERT INTO "
	_insertStrValues = " VALUES "
	_tableName = 'table.test'
	_valuesName = []
	_values = []
	_insertList = []

	def __init__(self,tableName,valuesName, arrayValues):
		self._tableName = tableName
		self._valuesName = valuesName
		self._values = arrayValues
		self._make()

	def _make(self):
		start = '('
		end = ');'
		value = ''
		valuesName = start

		for row in self._valuesName:
			valuesName += row + ","
		valuesName = valuesName[0:-1] + ")"

		for row in self._values:
			value=''
			for field in row:
				value = value + "'" + str(field) + "'" + ","
			sqlComplet = self._insertStr + self._tableName + valuesName + self._insertStrValues + start + value[0:-1] + end
			self._insertList.append(sqlComplet)

	def results(self):
		return self._insertList