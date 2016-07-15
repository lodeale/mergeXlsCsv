import itertools

class Merge(object):
	_arrayOne = []
	_arrayTwo = []
	_arrayOneHeader = []
	_arrayTwoHeader = []
	_arrayNameField = []
	_arrayCompleted = []
	_merged = []
	_idArray = []

	def __init__(self, arrayOne, arrayTwo, idData, arrayNameField):
		self._arrayOne = arrayOne
		self._arrayTwo = arrayTwo
		self._arrayOneHeader = arrayOne.pop(0)
		self._arrayTwoHeader = arrayTwo.pop(0)
		self._idArray = idData
		self._arrayNameField = arrayNameField
		self._merge()

	def _merge(self):
		#print "header1=> ",self._arrayOneHeader
		indexOne = self._arrayOneHeader.index(self._idArray[0])
		indexTwo = self._arrayTwoHeader.index(self._idArray[1])
		
		for rowOne in self._arrayOne:
			for rowTwo in self._arrayTwo:
				"""Error porque hay string con \n\r en el excel """
				try:
					if ( int(rowOne[indexOne]) == int(rowTwo[indexTwo]) ):
						rowNew = []
						for field in self._arrayNameField:
							if ( field in self._arrayOneHeader ):
								i = self._arrayOneHeader.index(field)
								rowNew.append(rowOne[i])
							elif ( field in self._arrayTwoHeader):
								i = self._arrayTwoHeader.index(field)
								rowNew.append(rowTwo[i])
						self._arrayCompleted.append(rowNew)
				except Exception as e:
					pass
					#print "Error: ",e
	def results(self):
		return self._arrayCompleted
	def count(self):
		return len(self._arrayCompleted)

		