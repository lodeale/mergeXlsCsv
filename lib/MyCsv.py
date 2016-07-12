import csv

class MyCsv(object):
	headerCsv = []
	bodyCsv = []
	
	def get(self,fileName):
		reader = csv.reader(open(fileName,'rb'))
		for index, row in enumerate(reader):
			self.bodyCsv.append(row)
		self.headerCsv = self.bodyCsv.pop(0)

	def show(self):
		print "HEADER:\n", self.headerCsv
		print "Body: \n" , self.bodyCsv