import re

from .getPublicData import *

def getRankData():
    cars = list(getAllCars())
    carData = []
    for car in cars:
        car.price = re.findall('\d+\.\d+', car.price)
        car.price = "-".join(car.price)
        carData.append({
            "brand": car.brand,
            "carName": car.carName,
            "rank": car.rank,
            "carImg": car.carImg,
            "manufacturer": car.manufacturer,
            "carModel": car.carModel,
            "price": car.price,
            "saleVolume": car.saleVolume,
            "marketTime":car.marketTime,
            "insure": car.insure
        })
    return carData
