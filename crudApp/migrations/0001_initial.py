# Generated by Django 4.0.4 on 2022-05-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=50)),
                ('sclass', models.IntegerField()),
                ('saddress', models.CharField(max_length=1000)),
            ],
        ),
    ]
