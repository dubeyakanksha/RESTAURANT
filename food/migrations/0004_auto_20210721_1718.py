# Generated by Django 3.1.7 on 2021-07-21 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_booktable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktable',
            name='persons',
            field=models.IntegerField(),
        ),
    ]
