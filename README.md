# Comparativo
Análisis Comparativo de Algoritmos utilizando ARBOLES Y DICCIONARIOS
# Sistema de Reserva de Aulas utilizando DICCIONAROS
### Importaciones y Diccionario de Aulas
```python
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
```

- `import datetime`: Importa el módulo datetime para trabajar con fechas y horas.
- `aulas`: Diccionario que almacena las aulas disponibles y sus reservas. Cada aula tiene una lista de reservas, que inicialmente está vacía o contiene reservas predefinidas.

### Función para Verificar la Disponibilidad del Aula

```python
def aula_libre(aula, inicio, fin):
    for reserva in aulas[aula]:
        if inicio < reserva['fin'] and fin > reserva['inicio']:
            return False
    return True
```

- `aula_libre(aula, inicio, fin)`: Verifica si un aula está libre en el intervalo de tiempo especificado. Devuelve `False` si hay un conflicto con otra reserva, `True` si el aula está libre.

### Función para Reservar un Aula

```python
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
```

- `reserva_aula()`: Solicita al usuario los detalles de la reserva (aula, inicio, fin, reservado por).
  - Verifica si el aula existe.
  - Solicita y valida las fechas de inicio y fin.
  - Comprueba si el aula está libre utilizando `aula_libre`.
  - Si está libre, agrega la reserva al diccionario `aulas`. Si no, informa al usuario que el aula ya está reservada.

### Bucle Principal del Programa

```python
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
```

- `while True`: Bucle infinito que mantiene el programa en ejecución hasta que el usuario decide salir.
- `opcion = input(...)`: Solicita al usuario que elija una opción.
  - `if opcion == '1'`: Muestra todas las aulas y su disponibilidad.
    - Recorre el diccionario `aulas` y muestra el estado (Libre/Ocupada) y detalles de las reservas si existen.
  - `elif opcion == '2'`: Llama a la función `reserva_aula` para gestionar una nueva reserva.
  - `elif opcion == '3'`: Imprime un mensaje de despedida y sale del bucle, terminando el programa.
  - `else`: Informa al usuario si la opción no es válida.

