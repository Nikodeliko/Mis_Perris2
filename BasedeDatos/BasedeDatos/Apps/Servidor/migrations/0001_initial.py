# Generated by Django 2.1 on 2018-10-25 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Ciudad', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Perros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Foto', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Raza_predominante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Raza', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Region', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_tipo_estado', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_Tipo_Vivienda', models.PositiveSmallIntegerField()),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.CharField(max_length=40)),
                ('Run', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Fecha_Nacimineto', models.DateField()),
                ('Fono', models.PositiveSmallIntegerField()),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servidor.Ciudad')),
                ('Region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servidor.Region')),
                ('Tipo_Vivienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Servidor.Tipo_Vivienda')),
            ],
        ),
        migrations.AddField(
            model_name='perros',
            name='Estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servidor.Tipo_estado'),
        ),
        migrations.AddField(
            model_name='perros',
            name='Raza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servidor.Raza_predominante'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='Region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Servidor.Region'),
        ),
    ]
