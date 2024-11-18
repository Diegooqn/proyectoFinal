class Conviviente:
    def __init__(self, nombre, parentesco, tiene_comorbilidades=False):
        self.nombre = nombre
        self.parentesco = parentesco
        self.tiene_comorbilidades = tiene_comorbilidades

class HistorialCovid:
    def __init__(self, ha_tenido_covid, fecha_contagio=None, nivel_afectacion=None):
        self.ha_tenido_covid = ha_tenido_covid
        self.fecha_contagio = fecha_contagio
        self.nivel_afectacion = nivel_afectacion  # leve, moderado, grave

class Empleado:
    def __init__(self, nombre, direccion, localidad):
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.convivientes = []  # lista de Conviviente
        self.registro_diario = []
        self.comorbilidades = []  # lista de strings con las comorbilidades
        self.historial_covid = None  # objeto HistorialCovid
        self.estado_salud = "saludable"  # saludable, enfermo, en_observacion

class RegistroDiario:
    def __init__(self, fecha, temperatura, sintomas, contacto_covid, estado_actual):
        self.fecha = fecha
        self.temperatura = temperatura
        self.sintomas = sintomas  # lista de síntomas
        self.contacto_covid = contacto_covid
        self.estado_actual = estado_actual  # cómo se siente hoy