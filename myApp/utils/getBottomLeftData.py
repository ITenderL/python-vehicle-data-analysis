import re

from .getPublicData import *


def getSquareData():
    cas = list(getAllCars())
    carsVolume = {}
    for car in cas:
        if carsVolume.get(car.carName, -1) == -1:
            carsVolume[car.carName] = car.saleVolume
        else:
            carsVolume[car.carName] += car.saleVolume
    sortedCars = sorted(carsVolume.items(), key=lambda x: x[1], reverse=True)[:15]
    brandList = []
    volumeList = []
    priceList = []
    for car in sortedCars:
        brandList.append(car[0])
        volumeList.append(car[1])
    for car in cas[:15]:
        car.price = re.findall('\d+\.\d+', car.price)
        car.price = car.price[0]
        priceList.append(float(car.price))
    print(priceList)
    return brandList, volumeList, priceList
