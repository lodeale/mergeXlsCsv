import itertools

class Merge(object):
	_arrayOne = []
	_arrayTwo = []
	_arrayOneHeader = []
	_arrayTwoHeader = []
	_idArray = []
	_arrayNameField = []
	_merged = []

	def __init__(self, arrayOne, arrayTwo, idData, arrayNameField):
		self._arrayOne = arrayOne
		self._arrayTwo = arrayTwo
		self._arrayOneHeader = arrayOne.pop(0)
		self._arrayTwoHeader = arrayTwo.pop(0)
		self._idArray = idData
		self._arrayNameField = arrayNameField
		self._merge()
	def _merge(self):
		print self._idArray,"alskjdflaskjd: ", self._arrayOneHeader, self._arrayTwoHeader
		indexOne = self._arrayOneHeader.index(self._idArray[0])
		indexTwo = self._arrayTwoHeader.index(self._idArray[1])
		rowNew = []
		
		for rowOne in self._arrayOne:
			for rowTwo in self._arrayTwo:
				try:
					if ( int(rowOne[indexOne]) == int(rowTwo[indexTwo]) ):
						#print "Son iguales: ", rowOne[indexOne],int(rowTwo[indexTwo])
						try:
							for pepe in self._arrayNameField:
								if ( self._arrayOneHeader.index(pepe) ):
									i = self._arrayOneHeader.index(pepe)
									print "alksdjf",i
									rowNew.append(rowOne[i])
								elif ( self._arrayTwoHeader.index(pepe)):
									i = self._arrayTwoHeader.index(pepe)
									print "else", i
									rowNew.append(rowTwo[i])
								else:
									print "Fuck"
						except:
							print "for fuck"
						print rowNew

				except:
					pass

		