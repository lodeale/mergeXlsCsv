import itertools
from Validate import Validate

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
		v = Validate()
		self._arrayOneHeader = v.clean(self._arrayOneHeader)
		indexOne = self._arrayOneHeader.index(self._idArray[0])
		indexTwo = self._arrayTwoHeader.index(self._idArray[1])
		cleanArrayOne = v.clean(self._arrayOne)
		cleanArrayTwo = v.clean(self._arrayTwo)

		for rowOne in cleanArrayOne:
			for rowTwo in cleanArrayTwo:
				try:
					if ( rowOne and rowTwo and rowOne != '' and rowTwo != '' and (int(rowOne[indexOne]) == int(rowTwo[indexTwo])) ):
						rowNew = []
						for field in self._arrayNameField:
							if ( field in self._arrayOneHeader ):
								i = self._arrayOneHeader.index(field)
								rowNew.append(rowOne[i])
							elif ( field in self._arrayTwoHeader):
								i = self._arrayTwoHeader.index(field)
								rowNew.append(rowTwo[i])
						self._arrayCompleted.append(rowNew)
					else:
						pass
				except Exception as e:
					print "Error: ",e
					
	def results(self):
		return self._arrayCompleted
	def count(self):
		return len(self._arrayCompleted)

		