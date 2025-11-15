from collections import deque

def bfs(grafo, origem):
    visitado = set()
    fila = deque([origem])
    ordem_visita = []

    visitado.add(origem)

    while fila:
        vertice = fila.popleft()
        ordem_visita.append(vertice)

        for vizinho in grafo[vertice]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

    return ordem_visita

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(grafo, 'A'))
