import funciones as fn 

trabajadores = [
    'Juan Pérez', 'Maria García', 'Carlos Lopez','Ana Martinez', 'Pedro Rodriguez', 
    'Laura Hernández','Miguel Sanchez', 'Isabel Gómez', 'Francisco Díaz', 'Elena Fernández' 
    ]

sueldo_trabajadores = {}

while True:
    try:
        print("0. Inicializar sueldos")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadisticas")
        print("4. Reporte de sueldos.")
        print("5. Salir del programa")
        opc = int(input("Ingrese su opción: "))
    except:
        print("Ha ocurrido un error, intente nuevamente.")
    
    if opc == 0:
        sueldo_trabajadores = {trabajador : 0 for trabajador in trabajadores}
        print("Sueldos inicializados")
    if opc == 1:
        sueldo_trabajadores = fn.asignar_sueldos_aleatorios(trabajadores)
    elif opc == 2:
        fn.clasificar_por_sueldo(sueldo_trabajadores)
    elif opc == 3:
        print("esta opción no se desarrolló")
    elif opc == 4:
        print("esta opción no se desarolló")
    elif opc == 5:
        break
