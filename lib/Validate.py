class Validate(object):
	_arrayFields = []
	def __init__(self,arrayValue):
		self._arrayFields = arrayValue
	def run(self):
		for field in self._arrayFields:
			print field
	def type(self,value):
		return type(value)