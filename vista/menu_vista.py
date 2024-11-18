class MenuVista:
    def mostrar_menu(self):
        print("\n=== Sistema de Control COVID ===")
        print("1. Agregar empleado")
        print("2. Agregar conviviente a empleado")
        print("3. Registrar historial COVID")
        print("4. Agregar comorbilidad")
        print("5. Registrar datos diarios")
        print("6. Actualizar estado de salud")
        print("7. Verificar estado de empleado")
        print("8. Ver detalles de empleado")
        print("9. Salir")
        return input("Seleccione una opción: ")
    
    def pedir_datos_empleado(self):
        nombre = input("Nombre del empleado: ")
        direccion = input("Dirección: ")
        localidad = input("Localidad: ")
        return nombre, direccion, localidad
    
    def pedir_datos_conviviente(self):
        nombre = input("Nombre del conviviente: ")
        parentesco = input("Parentesco: ")
        tiene_comorb = input("¿Tiene comorbilidades? (s/n): ").lower() == 's'
        return nombre, parentesco, tiene_comorb
    
    def pedir_datos_covid(self):
        ha_tenido = input("¿Ha tenido COVID? (s/n): ").lower() == 's'
        if ha_tenido:
            fecha = input("Fecha de contagio (DD/MM/AAAA): ")
            nivel = input("Nivel de afectación (leve/moderado/grave): ")
            return ha_tenido, fecha, nivel
        return ha_tenido, None, None
    
    def pedir_datos_registro(self):
        from datetime import datetime
        fecha = datetime.now()
        temperatura = float(input("Temperatura actual: "))
        print("Síntomas (separados por coma si hay varios): ")
        sintomas = [s.strip() for s in input().split(',') if s.strip()]
        contacto = input("¿Ha tenido contacto con casos positivos? (s/n): ").lower() == 's'
        estado = input("¿Cómo se siente hoy? ")
        return fecha, temperatura, sintomas, contacto, estado