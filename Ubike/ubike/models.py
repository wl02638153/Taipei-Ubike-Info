from django.db import models


# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver 192.168.1.115:8000
# Create your models here.

class Ubike_Info(models.Model):
    sno = models.IntegerField(primary_key=True)
    sna = models.TextField(null=True)
    sarea = models.TextField(null=True)
    lat = models.TextField(null=True)
    lng = models.TextField(null=True)
    ar = models.TextField(null=True)
    sareaen = models.TextField(null=True)
    snaen = models.TextField(null=True)
    aren = models.TextField(null=True)

    class Meta:
        db_table = "Ubike_info"

    def __str__(self):
        return self.sna


class Ubike_Data(models.Model):
    seq = models.AutoField(primary_key=True, max_length=50)
    sno = models.ForeignKey(Ubike_Info, on_delete=models.CASCADE, to_field='sno', related_name='snos',
                            related_query_name="snos_query", )
    tot = models.TextField(null=True)
    sbi = models.TextField(null=True)
    bemp = models.TextField(null=True)
    act = models.TextField(null=True)
    utime = models.DateTimeField(null=True)

    class Meta:
        db_table = "Ubike_data"

    def __str__(self):
        return self.tot
