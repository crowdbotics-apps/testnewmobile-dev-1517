# Generated by Django 2.2.9 on 2020-01-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='KK',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kk', models.BigIntegerField()),
            ],
        ),
    ]
