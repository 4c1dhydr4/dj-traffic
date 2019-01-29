# Generated by Django 2.0.4 on 2018-05-01 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(help_text='Ingrese la IP estática de la Cámara', max_length=20)),
                ('orientation', models.CharField(help_text='Ingrese la Orientación según coordenadas (Ejemplo: Vertical)', max_length=20)),
                ('location', models.CharField(help_text='Locación exacta de la Cámara', max_length=50)),
                ('url', models.CharField(help_text='URL de Acceso', max_length=100)),
                ('active', models.BooleanField(default=False, help_text='Estado (Marcar para Activo)')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('cars', models.SmallIntegerField()),
                ('status', models.BooleanField()),
                ('duration', models.DecimalField(decimal_places=2, max_digits=5)),
                ('changesNumber', models.SmallIntegerField()),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='traffic.Camera')),
            ],
        ),
    ]
