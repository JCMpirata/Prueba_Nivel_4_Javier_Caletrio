import sys

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for columna in range(vertices)]
                      for fila in range(vertices)]

    def imprimir_arbol_expansion_maximo(self, parent):
        print("Arista \tPeso")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.grafo[i][parent[i]])

    def obtener_indice_personaje(self, personaje):
        for i in range(self.V):
            if personaje == personajes[i]:
                return i
        return -1

    def obtener_personajes_por_numero_episodio(self, num_episodio):
        pares_personajes = []
        for i in range(self.V):
            for j in range(i + 1, self.V):
                if self.grafo[i][j] == num_episodio:
                    pares_personajes.append((personajes[i], personajes[j]))
        return pares_personajes

    def obtener_personajes_por_numero_episodios(self, num_episodios):
        personajes_episodios = []
        for i in range(self.V):
            count = 0
            for j in range(self.V):
                count += self.grafo[i][j]
            if count == num_episodios:
                personajes_episodios.append(personajes[i])
        return personajes_episodios

    def obtener_arista_maxima(self, key, mstSet):
        maximo = -sys.maxsize - 1
        for v in range(self.V):
            if key[v] > maximo and mstSet[v] == False:
                maximo = key[v]
                max_index = v
        return max_index

    def arbol_expansion_maximo(self, origen):
        key = [-sys.maxsize - 1] * self.V
        parent = [None] * self.V
        key[origen] = 0
        mstSet = [False] * self.V
        parent[origen] = -1
        for cout in range(self.V):
            u = self.obtener_arista_maxima(key, mstSet)
            mstSet[u] = True
            for v in range(self.V):
                if (
                    self.grafo[u][v] > 0
                    and mstSet[v] == False
                    and key[v] < self.grafo[u][v]
                ):
                    key[v] = self.grafo[u][v]
                    parent[v] = u
        self.imprimir_arbol_expansion_maximo(parent)

if __name__ == "__main__":

    personajes = [
    "Iron-Man", "Hulk", "Khan", "Thor", "Capitan America", "Ant-Man", "Nick Fury", "The Winter Soldier",  # Agrega todos los personajes aquí
    # ...
    ]

    grafo = Grafo(8)  # Actualiza el tamaño de la matriz según tus necesidades

    # Agrega los pesos de las aristas según los episodios en los que aparecieron juntos los personajes
    grafo.grafo = [
        [0, 6, 0, 1, 8, 7, 3, 2],
        [6, 0, 0, 6, 1, 8, 9, 1],
        [0, 0, 0, 1, 2, 1, 5, 0],
        [1, 6, 1, 0, 1, 5, 9, 3],
        [8, 1, 2, 1, 0, 2, 4, 5],
        [7, 8, 1, 5, 2, 0, 1, 6],
        [3, 9, 5, 9, 4, 1, 0, 1],
        [2, 1, 0, 3, 5, 6, 1, 0],
    ]

    # Tarea 1: Hallar el árbol de expansión máximo desde el vértice que contiene a Iron-Man, Thor y The Winter Soldier
    inicio1 = grafo.obtener_indice_personaje("Iron-Man")
    grafo.arbol_expansion_maximo(inicio1)
    inicio2 = grafo.obtener_indice_personaje("Thor")
    grafo.arbol_expansion_maximo(inicio2)
    inicio3 = grafo.obtener_indice_personaje("The Winter Soldier")
    grafo.arbol_expansion_maximo(inicio3)

    # Tarea 2: Determinar el número máximo de episodio que comparten dos personajes e indicar los pares de personajes
    max_episodios = max(map(max, grafo.grafo))
    pares_personajes = grafo.obtener_personajes_por_numero_episodio(max_episodios)
    print("Número máximo de episodios compartidos:", max_episodios)
    print("Pares de personajes:", pares_personajes)

    # Tarea 3: Cargar todos los personajes
    print("Personajes:", personajes)

    # Tarea 4: Indicar qué personajes aparecieron en nueve episodios de la saga
    personajes_9_episodios = grafo.obtener_personajes_por_numero_episodios(9)
    print("Personajes que aparecieron en nueve episodios:", personajes_9_episodios)
