from django.http import JsonResponse

from .utils import getBottomLeftData
from .utils import getCenterData
from .utils import getCenterLeftData
from .utils import getCenterRightData
from .utils import getCenterRightDataChange
from .utils import getBottomRightData


# Create your views here.

def center(request):
    if request.method == "GET":
        sumCars, hignVolumeCars, topCar, mostModel, mostBrand, avgPrice = getCenterData.getbaseData()
        brandRanking = getCenterData.getRollDatas()
        oilRate, electricRate, mixedRate = getCenterData.getEnergyTypeRate()
        return JsonResponse(
            {
                'sumCars': sumCars,
                'hignVolumeCars': hignVolumeCars,
                'topCar': topCar,
                'mostModel': mostModel,
                'mostBrand': mostBrand,
                'avgPrice': avgPrice,
                'brandRanking': brandRanking,
                'oilRate': oilRate,
                'electricRate': electricRate,
                'mixedRate': mixedRate
            }
        )


def centerLeft(request):
    if request.method == "GET":
        pieListData = getCenterLeftData.getPieBrandData()
        return JsonResponse(
            {
                'pieListData': pieListData
            }
        )


def bottomLeft(request):
    if request.method == "GET":
        brandList, volumeList, priceList = getBottomLeftData.getSquareData()
        return JsonResponse(
            {
                'brandList': brandList,
                'volumeList': volumeList,
                'priceList': priceList
            }
        )


def centerRight(request):
    if request.method == "GET":
        priceSortList = getCenterRightData.getPriceSortData()
        return JsonResponse(
            {
                'priceSortList': priceSortList
            }
        )


def centerRightChange(request, energyType):
    if request.method == "GET":
        oilData, electricityData = getCenterRightDataChange.getEnergyTypeCarData()
        result = []
        if energyType == 1:
            result = oilData
        elif energyType == 2:
            result = electricityData
        return JsonResponse(
            {
                'result': result,
            }
        )


def bottomRight(request):
    if request.method == "GET":
        carData = getBottomRightData.getRankData()
        return JsonResponse(
            {
                'carData': carData,
            }
        )
