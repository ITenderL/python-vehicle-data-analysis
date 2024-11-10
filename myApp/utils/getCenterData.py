import json

from .getPublicData import *


def getbaseData():
    cars = list(getAllCars())
    sumCars = len(cars)
    hignVolumeCars = cars[0].saleVolume
    topCar = cars[0].carName
    # 车型
    carModels = {}
    maxModel = 0
    mostModel = ""
    for car in cars:
        if carModels.get(car.carModel, -1) == -1:
            carModels[str(car.carModel)] = 1
        else:
            carModels[str(car.carModel)] += 1
    carModels = sorted(carModels.items(), key=lambda x: x[1], reverse=True)
    mostModel = carModels[0][0]
    # 品牌
    carBrand = {}
    maxBrand = 0
    mostBrand = ""
    for car in cars:
        if carBrand.get(car.brand, -1) == -1:
            carBrand[str(car.brand)] = 1
        else:
            carBrand[str(car.brand)] += 1
    sorted(carBrand.items(), key=lambda x: x[1], reverse=True)
    for k, v in carBrand.items():
        if v > maxBrand:
            maxBrand = v
            mostBrand = k
    # 车辆平均价格
    carPrice = {}
    avgPrice = 0
    sumPrice = 0
    for car in cars:
        x = json.loads(car.price)[0] + json.loads(car.price)[1]
        sumPrice += x
    avgPrice = sumPrice / (sumCars * 2)
    avgPrice = round(avgPrice, 2)
    return sumCars, hignVolumeCars, topCar, mostModel, mostBrand, avgPrice


def getRollDatas():
    cars = list(getAllCars())
    carBrands = {}
    for car in cars:
        if carBrands.get(car.brand, -1) == -1:
            carBrands[str(car.brand)] = 1
        else:
            carBrands[str(car.brand)] += 1
    brandList = [(key, value) for key, value in carBrands.items()]
    brandList.sort(key=lambda x: x[1], reverse=True)
    # sortDict = {data[0]: data[1] for data in brandList[:10]}
    brandRanking = []
    for data in brandList[:10]:
        brandRanking.append({"name": data[0], "value": data[1]})
    # print(brandRanking)
    return brandRanking


def getEnergyTypeRate():
    cars = list(getAllCars())
    carTypes = {}
    for car in cars:
        if carTypes.get(car.energyType, -1) == -1:
            carTypes[str(car.energyType)] = 1
        else:
            carTypes[str(car.energyType)] += 1
    oilRate = round(carTypes.get("汽油", 0) / len(cars) * 100, 2)
    electricRate = round(carTypes.get("纯电动", 0) / len(cars) * 100, 2)
    mixedRate = round((len(cars) - carTypes.get("汽油", 0) - carTypes.get("纯电动", 0)) / len(cars) * 100, 2)
    print(oilRate, electricRate, mixedRate)
    return oilRate, electricRate, mixedRate
