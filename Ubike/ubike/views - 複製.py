from django.shortcuts import render
import pymysql


# Create your views here.
def ubike_data(request):
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='****',
        db='ubike',
        charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM ubike_info ORDER BY sno")
    cursor_data = db.cursor(pymysql.cursors.DictCursor)
    cursor_data.execute("SELECT * FROM ubike_data ORDER BY sno")
    try:
        ubike_data = cursor.fetchall()

    finally:
        db.close()

    return render(request, "ubike_data.html", locals())


def ubike_detil(request):
    db = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='****',
        db='ubike',
        charset='utf8'
    )
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM ubike_info ORDER BY sno")
    try:
        ubike_data = cursor.fetchall()

    finally:
        db.close()

    return render(request, "ubike_data.html", locals())


def NB_IoT(request):
    return render(request, 'nb-iot.html')
