from myApp.models import *


def getAllCars():
    return CarInfo.objects.all()

