import re

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

	def clean(self, elements):
		elementsTrue = []
		result = []
		pattern = re.compile("\'")
		pattern2 = re.compile("\n")
		#try:
		if ( type(elements) is list):
			for subElement in elements:
				if ( type(subElement) is list ):
					subElementsTrue = []
					for ele in subElement:
						#is None?
						if ( ele is None ):
							ele = str(ele)
						if ( type(ele) is str):
							if ( pattern.findall(ele) > 0 ):
								ele = ele.replace("'","")
							ele.replace("\n","")
						subElementsTrue.append(ele)
					elementsTrue.append(subElementsTrue)
				else:
					#is None?
					if ( subElement is None ):
						subElement = str(subElement)
					#if is str and find ' in string
					if ( type(subElement) is str):
						if (pattern.findall(subElement) > 0 ):
							subElement = subElement.replace("'","")
					elementsTrue.append(subElement)
		elif ( type(elements) is str):
			if ( pattern.findall(elements) > 0 ):
				ele = elements.replace("'","")
				elementsTrue.append(ele)
		result = elementsTrue
		#except Exception, e:
		#	"Print error manejado: ", e
		#	raise
		return result

	def type(self,value):
		return type(value)
	def errorValidate(self):
		return self._errorValidate