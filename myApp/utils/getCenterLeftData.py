from .getPublicData import *

def getPieBrandData():
    cars = list(getAllCars())
    carVolume = {}
    for car in cars:
        if carVolume.get(car.brand, -1) == -1:
            carVolume[str(car.brand)] = int(car.saleVolume)
        else:
            carVolume[str(car.brand)] += int(car.saleVolume)
    pieListData = []
    sortedCars = sorted(zip(carVolume.values(), carVolume.keys()), reverse=True)
    print(sortedCars)
    for sortedCar in sortedCars:
        pieListData.append({"name": sortedCar[1], "value": sortedCar[0]})
    return pieListData[:10]