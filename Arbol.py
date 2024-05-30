import datetime

class Node:
    __slots__ = ('value', 'reservas', 'children')

    def __init__(self, value):
        self.value = value
        self.reservas = []
        self.children = [None, None]

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

def aula_libre(aula, inicio, fin):
    node = arbol_aulas.buscar_aula(aula)
    return node is not None and not any(inicio < reserva['fin'] and fin > reserva['inicio'] for reserva in node.reservas)

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

arbol_aulas = Tree()
aulas_iniciales = ["Aula de Programación", "Laboratorio de Bases de Datos", "Sala de Desarrollo Web",
                   "Aula de Inteligencia Artificial", "Laboratorio de Redes", "Aula de Realidad Virtual",
                   "Aula de Ciberseguridad", "Sala de Robótica"]

for aula in aulas_iniciales:
    arbol_aulas.add_aula(aula)

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