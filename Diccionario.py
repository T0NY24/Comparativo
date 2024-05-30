import datetime
aulas = {
    "Aula de Programación": [],
    "Laboratorio de Bases de Datos": [],
    "Sala de Desarrollo Web": [],
    "Aula de Inteligencia Artificial": [],
    "Laboratorio de Redes": [],
    "Aula de Realidad Virtual": [{'inicio': datetime.datetime(2024, 5, 29, 9, 0), 'fin': datetime.datetime(2024, 5, 29, 12, 0), 'reservado_por': 'Profesor X'}],
    "Aula de Ciberseguridad": [{'inicio': datetime.datetime(2024, 5, 29, 13, 0), 'fin': datetime.datetime(2024, 5, 29, 15, 0), 'reservado_por': 'Profesor Y'}],
    "Sala de Robótica": [{'inicio': datetime.datetime(2024, 5, 29, 10, 0), 'fin': datetime.datetime(2024, 5, 29, 14, 0), 'reservado_por': 'Profesor Z'}]
}
def aula_libre(aula, inicio, fin):
    for reserva in aulas[aula]:
        if inicio < reserva['fin'] and fin > reserva['inicio']:
            return False
    return True
def reserva_aula():
    aula = input("¿Qué aula quieres reservar? ").strip()
    if aula not in aulas:
        print("¡Esa aula no existe!")
        return

    while True:
        try:
            inicio = datetime.datetime.strptime(input("¿Cuándo quieres reservarla? (YYYY-MM-DD HH:MM) "), "%Y-%m-%d %H:%M")
            fin = datetime.datetime.strptime(input("¿Hasta cuándo? (YYYY-MM-DD HH:MM) "), "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("¡Esa no es una fecha válida! Inténtalo de nuevo.")

    reservado_por = input("¿Quién la va a reservar? ").strip()

    if aula_libre(aula, inicio, fin):
        aulas[aula].append({
            'inicio': inicio,
            'fin': fin,
            'reservado_por': reservado_por
        })
        print(f"¡{aula} reservada desde {inicio} hasta {fin} por {reservado_por}!")
    else:
        print("¡Ups! Alguien ya reservó esa aula en ese horario.")
while True:
    opcion = input("¿Qué quieres hacer?\n1. Ver aulas\n2. Reservar un aula\n3. Salir\n").strip()

    if opcion == '1':
        for aula, reservas in aulas.items():
            print(f"\nAula: {aula}")
            if reservas:
                print("  Estado: Ocupada")
                for reserva in reservas:
                    print(f"  - Desde: {reserva['inicio']} Hasta: {reserva['fin']} Reservado por: {reserva['reservado_por']}")
            else:
                print("  Estado: Libre")
    elif opcion == '2':
        reserva_aula()
    elif opcion == '3':
        print("¡Adiós!")
        break
    else:
        print("¡Esa no es una opción válida! Inténtalo de nuevo.")