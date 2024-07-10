import random

def asignar_sueldos_aleatorios(trabajadores):
    sueldo_trabajadores={}
    for trabajador in trabajadores:
        sueldo_trabajador = random.randint(300000, 2400000)
        sueldo_trabajadores[trabajador]=sueldo_trabajador
    print(sueldo_trabajadores)
    return sueldo_trabajadores

def clasificar_por_sueldo(sueldo_trabajadores):
    menoresque800 = {}
    entre800y2000 = {}
    mayorque2000 = {}
    for trabajador, sueldo_trabajador in sueldo_trabajadores.items():
        if sueldo_trabajador < 800000:
            menoresque800[trabajador] = sueldo_trabajador
        elif sueldo_trabajador <= 2000000:
            entre800y2000[trabajador] = sueldo_trabajador
        elif sueldo_trabajador > 2000000:
            mayorque2000[trabajador] = sueldo_trabajador
    print("Sueldos menores a 800.000 en total: ",len(menoresque800))
    for trabajador, sueldo_trabajador in menoresque800.items():
        print(trabajador,": $",sueldo_trabajador)
    print("Sueldos entre $800.000 y $2.000.000", len(entre800y2000))
    for trabajador, sueldo_trabajador in entre800y2000.items():
        print(trabajador,": $",sueldo_trabajador)
    print("Sueldos mayores que $2.000.000")
    for trabajador, sueldo_trabajador in mayorque2000.items():
        print(trabajador,": $",sueldo_trabajador)
        