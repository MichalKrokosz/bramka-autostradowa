class Car:
    def __init__(self, carID, plate, model, color, toPay):
        self.carID = carID;
        self.plate = plate
        self.model = model
        self.color = color
        self.toPay = toPay

    def getPlate(self):
        return self.plate
    
    def getToPay(self):
        return self.toPay
    
    def getCarID(self):
        return self.carID