# Generated by Django 3.1.2 on 2020-10-28 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='insumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipousuario')),
            ],
        ),
    ]
