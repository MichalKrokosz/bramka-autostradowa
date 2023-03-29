class Car:
	def __init__(self, name, plate, toPay):
		self.name = name
		self.plate = plate
		self.toPay = toPay
		
	def getPlate(self):
		return self.plate
	
	def getToPay(self):
		return self.toPay       