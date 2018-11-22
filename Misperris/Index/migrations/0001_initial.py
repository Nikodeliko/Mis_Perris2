# Generated by Django 2.1.3 on 2018-11-22 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.CharField(max_length=40)),
                ('Run', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Fecha_Nacimiento', models.DateField()),
                ('Fono', models.PositiveSmallIntegerField()),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Index.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.CharField(default='Invitado', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='formulario',
            name='Region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Index.Region'),
        ),
        migrations.AddField(
            model_name='formulario',
            name='Tipo_Vivienda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Index.Tipo_Vivienda'),
        ),
    ]
