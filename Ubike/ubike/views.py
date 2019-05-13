from django.shortcuts import render
from ubike.models import Ubike_Info, Ubike_Data

import datetime

import pymysql

today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)


def get_client_ip(request):
    # print(request.META)
    # print("HTTP_HOST",request.META.get('HTTP_HOST'))
    print("REMOTE_ADDR", request.META.get('REMOTE_ADDR'))
    ip = request.META.get('REMOTE_ADDR')
    return ip


def post_detail(request, pk):
    get_client_ip(request)
    post_ubike_info = Ubike_Info.objects.get(pk=pk)  # 取得該站資訊
    post_ubike_detail = Ubike_Info.objects.get(sno=pk).snos.all()  # 取得該站所有資料
    # date = post_ubike_detail.filter(utime__year='2018', utime__month='08',
    #                                utime__day='24')
    date = post_ubike_detail.filter(utime__range=(today_min, today_max))
    # print("date=", date)
    post_ubike_all = post_ubike_detail[0].tot  # 取得場站總停車格
    start = date[0].utime
    end = date.order_by('-seq')[0].utime
    # print(start)
    # print(end)
    now_sbi = post_ubike_detail.order_by('-seq')[0].sbi
    total = post_ubike_detail.order_by('-seq')[0].tot
    return render(request, 'ubike_detail.html',
                  {'post_ubike_info': post_ubike_info, 'post_ubike_detail': date,
                   'post_ubike_all': post_ubike_all, 'start': start, 'end': end, 'now_sbi': now_sbi, 'total': total})


def ubike_data_ORM(request):
    get_client_ip(request)
    ubike_list = Ubike_Info.objects.all()
    # print(ubike_list)

    return render(request, 'ubike_data.html', {'ubike_data': ubike_list})


# Create your views here.
def ubike_data(request):  # sql query
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


def ubike_detail(request):  # sql query
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
    get_client_ip(request)
    return render(request, 'nb-iot.html')
