class Validate(object):
	_errorValidate = []

	def __init__(self):
		pass
		
	def verify(self,value):
		try:
			if ( type(value) == 'str' or type(value) == 'unicode' ):
				value = value.decode("utf-8").replace("\n"," ")
				value = value.decode("utf-8").replace("\r"," ")
			else:
				return value
		except Exception, e:
			self._errorValidate.append(value)
		
		return value

	def type(self,value):
		return type(value)
	def errorValidate(self):
		return self._errorValidate