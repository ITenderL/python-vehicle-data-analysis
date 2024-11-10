import json

from .getPublicData import *


def getPriceSortData():
    cars = list(getAllCars())
    priceSortDict = {'0-5w': 0, '6-10w': 0, '10-20w': 0, '20-30w': 0, '30w以上': 0}
    for car in cars:
        price = [json.loads(car.price)[0]][0]
        if price < 5:
            priceSortDict['0-5w'] += 1
        elif price >= 5 and price < 10:
            priceSortDict['6-10w'] += 1
        elif price >= 10 and price <= 20:
            priceSortDict['10-20w'] += 1
        elif price >= 20 and price < 30:
            priceSortDict['20-30w'] += 1
        else:
            priceSortDict['30w以上'] += 1
    priceSortList = []
    for key, value in priceSortDict.items():
        priceSortList.append({'name': key, 'value': value})
    return priceSortList
