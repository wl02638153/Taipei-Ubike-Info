# Generated by Django 2.1 on 2018-08-23 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ubike_data',
            fields=[
                ('index', models.AutoField(max_length=50, primary_key=True, serialize=False)),
                ('tot', models.TextField(null=True)),
                ('sbi', models.TextField(null=True)),
                ('bemp', models.TextField(null=True)),
                ('act', models.TextField(null=True)),
                ('utime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'Ubike_data',
            },
        ),
        migrations.CreateModel(
            name='Ubike_info',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('sna', models.TextField(null=True)),
                ('sarea', models.TextField(null=True)),
                ('lat', models.TextField(null=True)),
                ('lng', models.TextField(null=True)),
                ('ar', models.TextField(null=True)),
                ('sareaen', models.TextField(null=True)),
                ('snaen', models.TextField(null=True)),
                ('aren', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Ubike_info',
            },
        ),
        migrations.AddField(
            model_name='ubike_data',
            name='sno',
            field=models.ForeignKey(db_column='sno', on_delete=django.db.models.deletion.CASCADE, related_name='snos', to='ubike.Ubike_info'),
        ),
    ]
