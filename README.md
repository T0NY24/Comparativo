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

# Sistema de Reserva de Aulas Usando Arbol

Este es un sistema de reserva de aulas implementado en Python utilizando una estructura de datos tipo árbol binario. Permite a los usuarios ver la disponibilidad de las aulas, reservarlas y salir del sistema.

## Descripción del Código

### Importaciones y Definición de Clases

```python
import datetime
```

- `import datetime`: Importa el módulo datetime para trabajar con fechas y horas.

```python
class Node:
    __slots__ = ('value', 'reservas', 'children')

    def __init__(self, value):
        self.value = value
        self.reservas = []
        self.children = [None, None]
```

- `class Node`: Define un nodo del árbol.
  - `__slots__`: Optimiza el uso de memoria restringiendo los atributos que pueden tener los objetos.
  - `__init__(self, value)`: Inicializa el nodo con un valor, una lista de reservas vacía y dos hijos (izquierdo y derecho) que inicialmente son `None`.

```python
class Tree:
    __slots__ = ('root',)

    def __init__(self):
        self.root = None

    def add_aula(self, aula):
        node = Node(aula)
        if not self.root:
            self.root = node
        else:
            self._add_node(self.root, node)

    def _add_node(self, parent, node):
        if node.value < parent.value:
            if not parent.children[0]:
                parent.children[0] = node
            else:
                self._add_node(parent.children[0], node)
        else:
            if not parent.children[1]:
                parent.children[1] = node
            else:
                self._add_node(parent.children[1], node)

    def buscar_aula(self, aula):
        return self._buscar_nodo(self.root, aula)

    def _buscar_nodo(self, node, aula):
        if not node:
            return None
        if node.value == aula:
            return node
        return self._buscar_nodo(node.children[0] if aula < node.value else node.children[1], aula)
```

- `class Tree`: Define el árbol binario.
  - `__slots__`: Optimiza el uso de memoria restringiendo los atributos que pueden tener los objetos.
  - `__init__(self)`: Inicializa el árbol con la raíz `root` como `None`.
  - `add_aula(self, aula)`: Añade un aula al árbol.
    - Crea un nuevo nodo con el valor del aula.
    - Si el árbol está vacío, el nodo se convierte en la raíz.
    - Si no, se llama a `_add_node` para colocar el nodo en la posición correcta.
  - `_add_node(self, parent, node)`: Función recursiva para añadir un nodo en la posición correcta del árbol.
  - `buscar_aula(self, aula)`: Busca un aula en el árbol y devuelve el nodo correspondiente.
  - `_buscar_nodo(self, node, aula)`: Función recursiva para buscar un nodo en el árbol.

### Función para Verificar la Disponibilidad del Aula

```python
def aula_libre(aula, inicio, fin):
    node = arbol_aulas.buscar_aula(aula)
    return node is not None and not any(inicio < reserva['fin'] and fin > reserva['inicio'] for reserva in node.reservas)
```

- `aula_libre(aula, inicio, fin)`: Verifica si un aula está libre en el intervalo de tiempo especificado.
  - Busca el nodo del aula en el árbol.
  - Devuelve `True` si el aula existe y no hay conflictos con otras reservas, `False` en caso contrario.

### Función para Reservar un Aula

```python
def reserva_aula():
    aula = input("¿Qué aula quieres reservar? ").strip()
    node = arbol_aulas.buscar_aula(aula)
    if not node:
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
        node.reservas.append({
            'inicio': inicio,
            'fin': fin,
            'reservado_por': reservado_por
        })
        print(f"¡{aula} reservada desde {inicio} hasta {fin} por {reservado_por}!")
    else:
        print("¡Ups! Alguien ya reservó esa aula en ese horario.")
```

- `reserva_aula()`: Solicita al usuario los detalles de la reserva (aula, inicio, fin, reservado por).
  - Verifica si el aula existe en el árbol.
  - Solicita y valida las fechas de inicio y fin.
  - Comprueba si el aula está libre utilizando `aula_libre`.
  - Si está libre, agrega la reserva al nodo correspondiente. Si no, informa al usuario que el aula ya está reservada.

### Inicialización del Árbol y Aulas Iniciales

```python
arbol_aulas = Tree()
aulas_iniciales = ["Aula de Programación", "Laboratorio de Bases de Datos", "Sala de Desarrollo Web",
                   "Aula de Inteligencia Artificial", "Laboratorio de Redes", "Aula de Realidad Virtual",
                   "Aula de Ciberseguridad", "Sala de Robótica"]

for aula in aulas_iniciales:
    arbol_aulas.add_aula(aula)
```

- `arbol_aulas = Tree()`: Crea una instancia del árbol.
- `aulas_iniciales`: Lista de nombres de aulas iniciales.
- Añade cada aula inicial al árbol.

### Reservas Iniciales

```python
aula_realidad_virtual = arbol_aulas.buscar_aula("Aula de Realidad Virtual")
aula_realidad_virtual.reservas.append({
    'inicio': datetime.datetime(2024, 5, 29, 9, 0),
    'fin': datetime.datetime(2024, 5, 29, 12, 0),
    'reservado_por': 'Profesor X'
})

aula_ciberseguridad = arbol_aulas.buscar_aula("Aula de Ciberseguridad")
aula_ciberseguridad.reservas.append({
    'inicio': datetime.datetime(2024, 5, 29, 13, 0),
    'fin': datetime.datetime(2024, 5, 29, 15, 0),
    'reservado_por': 'Profesor Y'
})

sala_robotica = arbol_aulas.buscar_aula("Sala de Robótica")
sala_robotica.reservas.append({
    'inicio': datetime.datetime(2024, 5, 29, 10, 0),
    'fin': datetime.datetime(2024, 5, 29, 14, 0),
    'reservado_por': 'Profesor Z'
})
```

- Añade reservas iniciales a algunas aulas para demostrar su uso.

### Bucle Principal del Programa

```python
while True:
    opcion = input("¿Qué quieres hacer?\n1. Ver aulas\n2. Reservar un aula\n3. Salir\n").strip()

    if opcion == '1':
        def imprimir_arbol(node):
            if node:
                print(f"\nAula: {node.value}")
                if node.reservas:
                    print("  Estado: Ocupada")
                    for reserva in node.reservas:
                        print(f"  - Desde: {reserva['inicio']} Hasta: {reserva['fin']} Reservado por: {reserva['reservado_por']}")
                else:
                    print("  Estado: Libre")
                imprimir_arbol(node.children[0])
                imprimir_arbol(node.children[1])

        imprimir_arbol(arbol_aulas.root)
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
    - `imprimir_arbol(node)`: Función recursiva para imprimir el árbol.
      - Recorre el árbol e imprime cada aula y su estado (Libre/Ocupada) junto con los detalles de las reservas si existen.
  - `elif opcion == '2'`: Llama a la función `reserva_aula` para gestionar una nueva reserva.
  - `elif opcion == '3'`: Imprime un mensaje de despedida y sale del bucle, terminando el programa.
  - `else`: Informa al usuario si la opción no es válida.

---

Este sistema de reservas te permite gestionar la disponibilidad de las aulas de manera eficiente utilizando una estructura de árbol binario, lo que facilita la búsqueda y gestión de las reservas.