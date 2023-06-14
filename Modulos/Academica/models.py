from django.db import models

class Idioma(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=6)

    def __str__(self):
        txt = "{0} (Duración: {1} mes(es))"
        return txt.format(self.nombre, self.duracion)

class Estudiante(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ("F", "Femenino"),
        ("M", "Masculino")
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default="F")
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)
    numeroCelular = models.CharField(max_length=15, default='123456789')
    correoElectronico = models.EmailField(default='example@example.com')
    region = models.CharField(max_length=50, default= "Lima")

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        txt = "{0} / Idioma: {1} / {2}"
        if self.vigencia:
            estadoEstudiante = "ACTIVO"
        else:
            estadoEstudiante = "INACTIVO"

        return txt.format(self.nombreCompleto(), self.idioma, estadoEstudiante)
        
   

class Docente(models.Model):
    dni = models.CharField(max_length=10, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    sexos = [
        ("F", "Femenino"),
        ("M", "Masculino")
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default="F")
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)
    numeroCelular = models.CharField(max_length=15, default='123456789')
    correoElectronico = models.EmailField(default='example@example.com')

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        txt = "{0} / Idioma: {1} / {2}"
        if self.vigencia:
            estadoDocente = "ACTIVO"
        else:
            estadoDocente = "INACTIVO"

        return txt.format(self.nombreCompleto(), self.idioma, estadoDocente)



class Nivel(models.Model):
    horario = models.CharField(max_length=30, primary_key=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE, default='PORTUGUES')
    frecuencia = models.CharField(max_length=30)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE, default="Nombre Docente")

    def __str__(self):
        return self.horario

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    horario = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='horarios', default="5:00-7:00PM")
    opciones_niveles = [
        ("B1", "Básico 1"),
        ("B2", "Básico 2"),
        ("B3", "Básico 3"),
        ("I1", "Intermedio 1"),
        ("I2", "Intermedio 2"),
        ("A", "Avanzado"),
    ]
    niveles = models.CharField(max_length=2, choices=opciones_niveles, default="B1")
    fechaMatricula = models.DateField()

    def __str__(self):
        txt = "{0}, {1}\t{2}\t{3}\t{4} matriculad{5} en el nivel {6} / Fecha: {7}"
        if self.estudiante.sexo == "F":
            letraSexo = "a"
        else:
            letraSexo = "o"
        fecMat = self.fechaMatricula.strftime("%d de %B de %Y")
        return txt.format(
            self.estudiante.apellidoPaterno, self.estudiante.apellidoMaterno,
            self.estudiante.nombres, self.estudiante.idioma.nombre,
            self.estudiante.vigencia, letraSexo, self.horario, fecMat
        )
