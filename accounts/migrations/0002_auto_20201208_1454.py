# Generated by Django 3.1.4 on 2020-12-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='docid',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]