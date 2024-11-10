import json

from .getPublicData import *


def getEnergyTypeCarData():
    cars = list(getAllCars())
    oilData = []
    electricityData = []
    for car in cars:
        if car.energyType == "汽油":
            oilData.append([car.carName, car.saleVolume, car.energyType])
        elif car.energyType == "纯电动":
            electricityData.append([car.carName, car.saleVolume, car.energyType])
    oilData = oilData[:10]
    electricityData = electricityData[:10]
    return oilData, electricityData
