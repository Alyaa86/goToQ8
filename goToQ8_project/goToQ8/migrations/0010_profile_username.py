# Generated by Django 2.0.5 on 2018-06-02 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goToQ8', '0009_auto_20180602_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
