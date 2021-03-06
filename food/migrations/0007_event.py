# Generated by Django 3.1.7 on 2021-08-05 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20210727_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('event', models.CharField(max_length=150)),
                ('persons', models.IntegerField()),
            ],
        ),
    ]
