# Generated by Django 3.1.2 on 2020-11-01 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('imagen', models.ImageField(null=True, upload_to='insumos')),
            ],
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vision', models.CharField(max_length=40)),
                ('Mision', models.CharField(max_length=40)),
            ],
        ),
    ]
