class GenerateSql(object):
	insertStr = "INSERT INTO %s VALUES "
	tableName = 'table.empresa'
	insertList = []

	def make(self,values):
		for row in values:
			start = '('
			end = ');'
			value = ''
			for field in row:
				#value = value + "\'" + str(field) + "\'" + ','
				value = value + str(field) + ','
			sqlComplet = self.insertStr + start + value[0:-1] + end
			self.insertList.append(sqlComplet)
			print sqlComplet