# Generated by Django 3.0 on 2023-06-22 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230607_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AlterField(
            model_name='song',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 22, 14, 27, 5, 139869)),
        ),
    ]
