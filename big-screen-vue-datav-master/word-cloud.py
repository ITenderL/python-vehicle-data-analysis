import jieba
import numpy as np
import pymysql
from PIL import Image
from matplotlib import pylab as plt

from wordcloud import WordCloud


def get_img(field, targetImageSrc, resImageSrc):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='cardata', charset='utf8mb4')
    cur = conn.cursor()
    sql = f"select {field} from t_car_info"
    cur.execute(sql)
    data = cur.fetchall()
    text = ''
    for d in data:
        if d[0] != None and d[0] != '':
            tagArr = d
            for tag in tagArr:
                text += tag

    cur.close()
    conn.close()
    data_cut = jieba.cut(text, cut_all=False)
    string = ' '.join(data_cut)
    # 生成词云
    img = Image.open(targetImageSrc)
    img_arr = np.array(img)
    wc = WordCloud(
        background_color='#04122c',
        mask=img_arr,
        font_path='STHUPO.TTF',
        max_words=2000
    )
    wc.generate_from_text(string)
    # 保存图片
    plt.figure(1)
    plt.imshow(wc)
    plt.axis('off')
    plt.savefig(resImageSrc, dpi=800)


get_img('manufacturer', './public/car.png',
        './public/car-wc.png')
