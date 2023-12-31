# Generated by Django 4.2.2 on 2023-06-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('apellidoPaterno', models.CharField(max_length=35)),
                ('apellidoMaterno', models.CharField(max_length=35)),
                ('nombres', models.CharField(max_length=35)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('vigencia', models.BooleanField(default=True)),
                ('numeroCelular', models.CharField(default='123456789', max_length=15)),
                ('correoElectronico', models.EmailField(default='example@example.com', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('dni', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('apellidoPaterno', models.CharField(max_length=35)),
                ('apellidoMaterno', models.CharField(max_length=35)),
                ('nombres', models.CharField(max_length=35)),
                ('fechaNacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='F', max_length=1)),
                ('vigencia', models.BooleanField(default=True)),
                ('numeroCelular', models.CharField(default='123456789', max_length=15)),
                ('correoElectronico', models.EmailField(default='example@example.com', max_length=254)),
                ('region', models.CharField(default='Lima', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('duracion', models.PositiveSmallIntegerField(default=6)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('horario', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('frecuencia', models.CharField(max_length=30)),
                ('docente', models.ForeignKey(default='Nombre Docente', on_delete=django.db.models.deletion.CASCADE, to='Academica.docente')),
                ('idioma', models.ForeignKey(default='PORTUGUES', on_delete=django.db.models.deletion.CASCADE, to='Academica.idioma')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('niveles', models.CharField(choices=[('B1', 'Básico 1'), ('B2', 'Básico 2'), ('B3', 'Básico 3'), ('I1', 'Intermedio 1'), ('I2', 'Intermedio 2'), ('A', 'Avanzado')], default='B1', max_length=2)),
                ('fechaMatricula', models.DateField()),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.estudiante')),
                ('horario', models.ForeignKey(default='5:00-7:00PM', on_delete=django.db.models.deletion.CASCADE, related_name='horarios', to='Academica.nivel')),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='idioma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.idioma'),
        ),
        migrations.AddField(
            model_name='docente',
            name='idioma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academica.idioma'),
        ),
    ]
