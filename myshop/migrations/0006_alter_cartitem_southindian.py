# Generated by Django 3.2.11 on 2024-01-27 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0005_auto_20240126_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='southindian',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myshop.southindian'),
        ),
    ]
