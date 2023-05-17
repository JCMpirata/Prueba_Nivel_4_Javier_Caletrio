import sys

class Grafo:
    def __init__(self, n):
        self.n = n
        self.matriz = [[sys.maxsize] * n for i in range(n)]
        self.visitados = [False] * n

    def agregar_arista(self, u, v, peso):
        self.matriz[u][v] = peso

    def floyd_warshall(self):
        distancias = [fila[:] for fila in self.matriz]
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])
        return distancias

    def encontrar_camino_mas_corto(self):
        distancias = self.floyd_warshall()
        actual = 0
        camino = [actual]
        self.visitados[actual] = True
        while len(camino) < self.n:
            siguiente = None
            distancia_minima = sys.maxsize
            for i in range(self.n):
                if not self.visitados[i]:
                    distancia = distancias[actual][i]
                    if distancia < distancia_minima:
                        siguiente = i
                        distancia_minima = distancia
            actual = siguiente
            self.visitados[actual] = True
            camino.append(actual)
        camino.append(0)
        return camino
    
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

    distancias = [
        [0, 675, 400, 166, 809, 720, 399, 233],
        [675, 0, 540, 687, 179, 348, 199, 401],
        [400, 540, 0, 107, 752, 521, 385, 280],
        [166, 687, 107, 0, 111, 540, 990, 361],
        [809, 179, 752, 111, 0, 206, 412, 576],
        [720, 348, 521, 540, 206, 0, 155, 621],
        [399, 199, 385, 990, 412, 155, 0, 100],
        [233, 401, 280, 361, 576, 621, 100, 0]
    ] 

    g = Grafo(len(nombres))

    for i in range(len(distancias)):
        for j in range(len(distancias[i])):
            g.agregar_arista(i, j, distancias[i][j])

    camino_mas_corto = g.encontrar_camino_mas_corto()
    
    print("El camino más corto es: ")
    for nodo in camino_mas_corto:
        print(nombres[nodo])
