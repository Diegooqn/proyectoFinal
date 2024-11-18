from controlador.empleado_controlador import EmpleadoControlador
from vista.menu_vista import MenuVista

def main():
    controlador = EmpleadoControlador()
    vista = MenuVista()
    
    while True:
        opcion = vista.mostrar_menu()
        
        if opcion == "1":
            datos = vista.pedir_datos_empleado()
            empleado = controlador.agregar_empleado(*datos)
            print(f"\nEmpleado {empleado.nombre} agregado correctamente")
            
        elif opcion == "2":
            if not controlador.empleados:
                print("\nNo hay empleados registrados")
                continue
            
            print("\nEmpleados disponibles:")
            for i, emp in enumerate(controlador.empleados):
                print(f"{i+1}. {emp.nombre}")
            
            idx = int(input("Seleccione el empleado: ")) - 1
            empleado = controlador.empleados[idx]
            
            datos = vista.pedir_datos_conviviente()
            controlador.agregar_conviviente(empleado, *datos)
            print("\nConviviente agregado correctamente")
            
        elif opcion == "3":
            if not controlador.empleados:
                print("\nNo hay empleados registrados")
                continue
            
            print("\nEmpleados disponibles:")
            for i, emp in enumerate(controlador.empleados):
                print(f"{i+1}. {emp.nombre}")
            
            idx = int(input("Seleccione el empleado: ")) - 1
            empleado = controlador.empleados[idx]
            
            datos = vista.pedir_datos_covid()
            controlador.registrar_historial_covid(empleado, *datos)
            print("\nHistorial COVID registrado")
            
        elif opcion == "4":
            if not controlador.empleados:
                print("\nNo hay empleados registrados")
                continue
            
            print("\nEmpleados disponibles:")
            for i, emp in enumerate(controlador.empleados):
                print(f"{i+1}. {emp.nombre}")
            
            idx = int(input("Seleccione el empleado: ")) - 1
            empleado = controlador.empleados[idx]
            
            comorbilidad = input("Ingrese la comorbilidad: ")
            controlador.agregar_comorbilidad(empleado, comorbilidad)
            print("\nComorbilidad agregada")
            
        elif opcion == "5":
            if not controlador.empleados:
                print("\nNo hay empleados registrados")
                continue
            
            print("\nEmpleados disponibles:")
            for i, emp in enumerate(controlador.empleados):
                print(f"{i+1}. {emp.nombre}")
            
            idx = int(input("Seleccione el empleado: ")) - 1
            empleado = controlador.empleados[idx]
            
            datos = vista.pedir_datos_registro()
            controlador.registrar_datos_diarios(empleado, *datos)
            print("\nRegistro diario guardado")
            
        elif opcion == "6":
            if not controlador.empleados:
                print("\nNo hay empleados registrados")
                continue
            
            print("\nEmpleados disponibles:")
            for i, emp in enumerate(controlador.empleados):
                print(f"{i+1}. {emp.nombre}")
            
            idx = int(input("Seleccione el empleado: ")) - 1
            empleado = controlador.empleados[idx]
            
            print("\nEstados disponibles:")
            print("1. Saludable")
            print("2. Enfermo")
            print("3. En observación")
            
            estado = input("Seleccione el nuevo estado: ")
            estados = ["saludable", "enfermo", "en_observacion"]
            if estado in "123":
                controlador.actualizar_estado_salud(empleado, estados[int(estado)-1])
                print("\nEstado actualizado")
            
        elif opcion == "7":
            if not controlador.empleados:
                print("\nNo hay empleados registrados")
                continue
            
            print("\nEmpleados disponibles:")
            for i, emp in enumerate(controlador.empleados):
                print(f"{i+1}. {emp.nombre}")
            
            idx = int(input("Seleccione el empleado: ")) - 1
            empleado = controlador.empleados[idx]
            
            puede = controlador.puede_trabajar(empleado)
            print(f"\n{empleado.nombre} {'puede' if puede else 'no puede'} trabajar hoy")
            
        elif opcion == "8":
            if not controlador.empleados:
                print("\nNo hay empleados registrados")
                continue
            
            print("\nEmpleados disponibles:")
            for i, emp in enumerate(controlador.empleados):
                print(f"{i+1}. {emp.nombre}")
            
            idx = int(input("Seleccione el empleado: ")) - 1
            empleado = controlador.empleados[idx]
            
            print(f"\nDetalles de {empleado.nombre}:")
            print(f"Dirección: {empleado.direccion}")
            print(f"Localidad: {empleado.localidad}")
            print(f"Estado de salud: {empleado.estado_salud}")
            print("\nConvivientes:")
            for conv in empleado.convivientes:
                print(f"- {conv.nombre} ({conv.parentesco})")
                if conv.tiene_comorbilidades:
                    print("  Tiene comorbilidades")
            
            print("\nComorbilidades:")
            for com in empleado.comorbilidades:
                print(f"- {com}")
            
            if empleado.historial_covid:
                print("\nHistorial COVID:")
                if empleado.historial_covid.ha_tenido_covid:
                    print(f"Fecha de contagio: {empleado.historial_covid.fecha_contagio}")
                    print(f"Nivel de afectación: {empleado.historial_covid.nivel_afectacion}")
                else:
                    print("No ha tenido COVID")
            
        elif opcion == "9":
            print("\n¡Hasta luego!")
            break
            
        else:
            print("\nOpción no válida")

if __name__ == "__main__":
    main()