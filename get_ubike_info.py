import requests
import json
import pymysql
from datetime import datetime

url = "http://data.taipei/youbike"
data = requests.get(url).json()

# for key, value in data["retVal"].items():
#     sno = value["sno"]
#     sna = value["sna"]
#     print("NO." + sno + " " + sna)

db = pymysql.Connect(
    host='192.168.1.116',
    port=3306,
    user='root',
    passwd='123password123',
    db='mydb',
    charset='utf8',
)
cursor = db.cursor()
for key, value in data["retVal"].items():
    sno = value["sno"]
    sna = value["sna"]
    sarea = value["sarea"]
    lat = value["lat"]
    lng = value["lng"]
    ar = value["ar"]
    sareaen = value["sareaen"]
    snaen = value["snaen"]
    aren = value["aren"]
    sql = "INSERT INTO Ubike_info(sno,sna,sarea,lat,lng,ar,sareaen,snaen,aren) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    try:
        cursor.execute(sql, (sno, sna, sarea, lat, lng, ar, sareaen, snaen, aren))
        db.commit()
        # print('成功插入', cursor.rowcount, '條資料')
    except:
        print("SQL", sql)
        print("DATA:", sno, sna, sarea, lat, lng, ar, sareaen, snaen, aren)
    finally:
        print("finally")

db.close()
