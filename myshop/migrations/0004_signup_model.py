# Generated by Django 4.2.6 on 2023-12-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Phone_No', models.IntegerField()),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=50)),
                ('Pincode', models.IntegerField()),
                ('State', models.CharField(max_length=50)),
            ],
        ),
    ]
