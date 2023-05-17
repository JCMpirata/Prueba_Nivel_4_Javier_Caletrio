class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adyacencias = [[] for _ in range(num_vertices)]

    def agregar_arista(self, u, v, peso):
        self.adyacencias[u].append((v, peso))
        self.adyacencias[v].append((u, peso))

    def aristas(self):
        aristas = []
        for u in range(self.num_vertices):
            for v, peso in self.adyacencias[u]:
                if u < v:
                    aristas.append((peso, u, v))
        return aristas

    def arbol_expansion_minimo_prim(self):
        visitados = [False] * self.num_vertices
        arbol = [-1] * self.num_vertices
        pesos = [float("inf")] * self.num_vertices
        pesos[0] = 0

        for _ in range(self.num_vertices):
            min_peso = float("inf")
            min_nodo = -1
            for v in range(self.num_vertices):
                if not visitados[v] and pesos[v] < min_peso:
                    min_peso = pesos[v]
                    min_nodo = v

            visitados[min_nodo] = True
            for v, peso in self.adyacencias[min_nodo]:
                if not visitados[v] and peso > pesos[v]:
                    pesos[v] = peso
                    arbol[v] = min_nodo

        return arbol

    def arbol_expansion_minimo_kruskal(self):
        aristas = self.aristas()
        aristas.sort(reverse=True)

        padre = list(range(self.num_vertices))

        def encontrar_raiz(u):
            while padre[u] != u:
                padre[u] = padre[padre[u]]
                u = padre[u]
            return u

        arbol = [-1] * self.num_vertices
        for peso, u, v in aristas:
            ru, rv = encontrar_raiz(u), encontrar_raiz(v)
            if ru != rv:
                arbol[v] = u
                padre[rv] = ru

        return arbol

    def existe_camino(self, origen, destino):
        visitados = [False] * self.num_vertices
        visitados[origen] = True

        def dfs(nodo):
            if nodo == destino:
                return True

            for v, _ in self.adyacencias[nodo]:
                if not visitados[v]:
                    visitados[v] = True
                    if dfs(v):
                        return True

            return False

        return dfs(origen)

    def seguidores_de(self, origen):
        visitados = [False] * self.num_vertices
        visitados[origen] = True
        seguidores = set()

        def bfs(nodo):
            for v, _ in self.adyacencias[nodo]:
                if not visitados[v]:
                    visitados[v] = True
                    seguidores.add(v)
                    bfs(v)

        bfs(origen)
        return seguidores

if __name__ == "__main__":
    nombres = [
        "Iron Man",
        "The increíble Hulk",
        "Khan",
        "Thor",
        "Captain América",
        "Ant-Man",
        "Nick Fury",
        "The Winter Soldier"
    ]

    twitter = [
        [0, 75, 40, 16, 80, 20, 99, 23],
        [75, 0, 50, 67, 79, 38, 99, 41],
        [40, 50, 0, 17, 75, 52, 85, 28],
        [16, 67, 17, 0, 11, 50, 90, 36],
        [80, 79, 75, 11, 0, 26, 12, 56],
        [20, 38, 52, 50, 26, 0, 55, 61],
        [99, 99, 85, 90, 12, 55, 0, 10],
        [23, 41, 28, 36, 56, 61, 10, 0]
    ]

    instagram = [
        [0, 61, 44, 66, 56, 74, 11, 65],
        [12, 0, 47, 41, 12, 38, 99, 41],
        [41, 23, 0, 45, 12, 89, 42, 14],
        [12, 69, 11, 0, 12, 50, 78, 63],
        [89, 19, 72, 11, 0, 26, 12, 56],
        [72, 34, 21, 65, 12, 0, 78, 41],
        [12, 87, 35, 99, 42, 15, 0, 10],
        [33, 41, 24, 61, 45, 41, 11, 0]
    ]

    grafo_twitter = Grafo(len(nombres))
    grafo_instagram = Grafo(len(nombres))

    for i in range(len(twitter)):
        for j in range(len(twitter[i])):
            if i != j:
                grafo_twitter.agregar_arista(i, j, twitter[i][j])
                grafo_instagram.agregar_arista(i, j, instagram[i][j])

    arbol_expansion_maxima_twitter = grafo_twitter.arbol_expansion_minimo_prim()
    arbol_expansion_maxima_instagram = grafo_instagram.arbol_expansion_minimo_prim()

    print("Árbol de expansión máxima en Twitter:")
    for i in range(1, len(arbol_expansion_maxima_twitter)):
        print(nombres[arbol_expansion_maxima_twitter[i]], "->", nombres[i])

    print("\nÁrbol de expansión máxima en Instagram:")
    for i in range(1, len(arbol_expansion_maxima_instagram)):
        print(nombres[arbol_expansion_maxima_instagram[i]], "->", nombres[i])

    capitana_marvel = nombres.index("Captain América")
    nick_fury = nombres.index("Nick Fury")
    winter_soldier = nombres.index("The Winter Soldier")
    iron_man = nombres.index("Iron Man")

    if grafo_twitter.existe_camino(capitana_marvel, nick_fury):
        print("\nEs posible conectar a Capitana Marvel con Nick Fury a través de Twitter.")
    else:
        print("\nNo es posible conectar a Capitana Marvel con Nick Fury a través de Twitter.")

    if grafo_twitter.existe_camino(winter_soldier, iron_man) or grafo_instagram.existe_camino(winter_soldier, iron_man):
        print("Es posible conectar a The Winter Soldier con Iron Man a través de alguna red social.")
    else:
        print("No es posible conectar a The Winter Soldier con Iron Man a través de ninguna red social.")

    thor = nombres.index("Thor")
    seguidores_instagram_thor = grafo_instagram.seguidores_de(thor)
    print("\nPersonas que sigue Thor en Instagram:")
    for seguidor in seguidores_instagram_thor:
        print(nombres[seguidor])

    seguidores_twitter_thor = grafo_twitter.seguidores_de(thor)
    print("\nPersonas que sigue Thor en Twitter:")
    for seguidor in seguidores_twitter_thor:
        print(nombres[seguidor])
