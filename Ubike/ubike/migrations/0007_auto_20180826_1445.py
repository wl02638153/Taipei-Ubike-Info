# Generated by Django 2.1 on 2018-08-26 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ubike', '0006_auto_20180826_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubike_data',
            name='sno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snos_set', to='ubike.Ubike_Info'),
        ),
    ]
