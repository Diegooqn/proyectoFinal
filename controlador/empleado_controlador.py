from modelo.empleado import Conviviente, HistorialCovid, Empleado, RegistroDiario


class EmpleadoControlador:
    def __init__(self):
        self.empleados = []
    
    def agregar_empleado(self, nombre, direccion, localidad):
        empleado = Empleado(nombre, direccion, localidad)
        self.empleados.append(empleado)
        return empleado
    
    def agregar_conviviente(self, empleado, nombre, parentesco, tiene_comorbilidades):
        conviviente = Conviviente(nombre, parentesco, tiene_comorbilidades)
        empleado.convivientes.append(conviviente)
    
    def registrar_historial_covid(self, empleado, ha_tenido, fecha=None, nivel=None):
        empleado.historial_covid = HistorialCovid(ha_tenido, fecha, nivel)
    
    def agregar_comorbilidad(self, empleado, comorbilidad):
        if comorbilidad not in empleado.comorbilidades:
            empleado.comorbilidades.append(comorbilidad)
    
    def registrar_datos_diarios(self, empleado, fecha, temperatura, sintomas, 
                              contacto_covid, estado_actual):
        registro = RegistroDiario(fecha, temperatura, sintomas, 
                                contacto_covid, estado_actual)
        empleado.registro_diario.append(registro)
        return registro
    
    def actualizar_estado_salud(self, empleado, nuevo_estado):
        empleado.estado_salud = nuevo_estado
    
    def puede_trabajar(self, empleado):
        if not empleado.registro_diario:
            return False
        
        ultimo_registro = empleado.registro_diario[-1]
        return (ultimo_registro.temperatura < 37.5 and 
                not ultimo_registro.sintomas and 
                not ultimo_registro.contacto_covid and
                empleado.estado_salud == "saludable")