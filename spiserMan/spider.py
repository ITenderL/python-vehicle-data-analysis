import csv
import os

from lxml import etree
import pandas as pd

import requests
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VehicleLargeScreenDisplay.settings')
django.setup()
from myApp.models import CarInfo


class spider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
        }
        self.spiderUrl = 'https://www.dongchedi.com/motor/pc/car/rank_data?aid=1839&app_name=auto_web_pc&city_name=%E5%8D%97%E4%BA%AC&count=10&month=&new_energy_type=&rank_data_type=11&brand_id=&price=&manufacturer=&outter_detail_type=&nation=0'

    def init(self):
        if not os.path.exists("./temp.csv"):
            with open('./temp.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                # 写入表头,字段不能用单引号
                writer.writerow(
                    ["brand", "carName", "carImg", "saleVolume", "price", "manufacturer", "rank", "carModel",
                     "energyType", "marketTime", "insure"]
                )

    def getPage(self):
        with open('./spiderPage.txt', 'r', encoding='utf-8') as f:
            return f.readlines()[-1].strip()

    def setPage(self, page):
        with open('./spiderPage.txt', 'a', encoding='utf-8') as f:
            f.write('\n' + str(page))

    def main(self):
        count = self.getPage()
        params = {
            'offset': int(count)
        }
        print("数据从{}开始爬取".format(int(count) + 1))
        pageJson = requests.get(self.spiderUrl, headers=self.headers, params=params).json()['data']['list']
        # self.setPage(int(count) + 10)
        try:
            for index, car in enumerate(pageJson):
                carData = []
                print("正在爬取第%d" % (index + 1) + "辆车")
                carData.append(car['brand_name'])
                carData.append(car['series_name'])
                carData.append(car['image'])
                carData.append(car['count'])
                price = []
                price.append(car['min_price'])
                price.append(car['max_price'])
                carData.append(price)
                carData.append(car['sub_brand_name'])
                carData.append(car['rank'])
                # 第二个页面
                carSeriesId = car['series_id']
                infoHTML = requests.get('https://www.dongchedi.com/auto/params-carIds-x-%s' % carSeriesId,
                                        headers=self.headers)
                inforHTMLpath = etree.HTML(infoHTML.text)
                carModel = inforHTMLpath.xpath("//div[@data-row-anchor='jb']/div[2]/div/text()")[0]
                carData.append(carModel)
                energyType = inforHTMLpath.xpath("//div[@data-row-anchor='fuel_form']/div[2]/div/text()")[0]
                carData.append(energyType)
                marketTime = inforHTMLpath.xpath("//div[@data-row-anchor='market_time']/div[2]/div/text()")[0]
                carData.append(marketTime)
                insure = inforHTMLpath.xpath("//div[@data-row-anchor='period']/div[2]/div/text()")[0]
                carData.append(insure)
                print(carData)
                self.save_to_csv(carData)
        except:
            pass
        self.setPage(int(count) + 10)
        self.main()

    def save_to_csv(self, resultData):
        with open('./temp.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(resultData)

    def clear_csv(self):
        df = pd.read_csv('./temp.csv')
        df.dropna(inplace=True)
        df.drop_duplicates()
        print("总数量为%d" % df.shape[0])
        return df.values

    def save_to_mysql(self):
        data = self.clear_csv()
        for car in data:
            CarInfo.objects.create(
                brand=car[0],
                carName=car[1],
                carImg=car[2],
                saleVolume=car[3],
                price=car[4],
                manufacturer=car[5],
                rank=car[6],
                carModel=car[7],
                energyType=car[8],
                marketTime=car[9],
                insure=car[10]
            )

if __name__ == '__main__':
    spiderObj = spider()
    # spiderObj.init()
    # spiderObj.main()
    spiderObj.save_to_mysql()