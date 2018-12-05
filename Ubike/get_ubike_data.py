from os import utime

import requests
import json
import pymysql
from datetime import datetime

url = "http://data.taipei/youbike"
newurl="https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.gz"
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0'}
try:
    data = requests.get(newurl, headers=headers).json()
    # data = requests.get(newurl).json()
except requests.exceptions.RequestException as e:
    print("錯誤", e)

db = pymysql.Connect(
    host='192.168.1.116',
    port=3306,
    user='root',
    passwd='123password123',
    db='mydb',
    charset='utf8'
)
cursor = db.cursor()
for key, value in data["retVal"].items():
    sno_id = value["sno"]
    tot = value["tot"]
    sbi = value["sbi"]
    bemp = value["bemp"]
    act = value["act"]
    sql = "INSERT INTO Ubike_data(sno_id,tot,sbi,bemp,act,utime) VALUES(%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql, (sno_id, tot, sbi, bemp, act, datetime.now()))
        db.commit()
        # print('成功插入', cursor.rowcount, '條資料')
    except pymysql.InternalError as e:
        print("ERROR:", e)
        print("SQL:", sql)
        print("DATA:", sno_id, tot, sbi, bemp, act, datetime.now())
        continue
    finally:
        print("finally")

sql = "DELETE FROM Ubike_data WHERE utime<=now() - interval 3 DAY "
try:
    cursor.execute(sql)
    db.commit()
except:
    print("delete failure")
finally:
    print("delete finally all")
#
db.close()
