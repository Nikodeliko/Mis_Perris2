# Generated by Django 2.1.2 on 2018-11-03 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Index', '0002_auto_20181028_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.CharField(max_length=40)),
                ('Run', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=100)),
                ('Apellido', models.CharField(max_length=100)),
                ('Fecha_Nacimineto', models.DateField()),
                ('Fono', models.PositiveSmallIntegerField()),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Index.Ciudad')),
                ('Region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Index.Region')),
                ('Tipo_Vivienda', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Index.Tipo_Vivienda')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Apellido',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Ciudad',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Fecha_Nacimineto',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Fono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Region',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Run',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='Tipo_Vivienda',
        ),
        migrations.AddField(
            model_name='usuario',
            name='perfil',
            field=models.CharField(default='Invitado', max_length=20),
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
