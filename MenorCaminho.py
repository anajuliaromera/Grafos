from collections import deque

def menor_caminho_bfs(grafo, origem, destino):
    visitado = set()
    fila = deque([origem])
    pais = {origem: None}  

    visitado.add(origem)

    while fila:
        atual = fila.popleft()

        if atual == destino:
            break

        for vizinho in grafo[atual]:
            if vizinho not in visitado:
                visitado.add(vizinho)
                pais[vizinho] = atual
                fila.append(vizinho)

    
    caminho = []
    atual = destino

    while atual is not None:
        caminho.append(atual)
        atual = pais.get(atual)

    caminho.reverse()
    return caminho

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(menor_caminho_bfs(grafo, 'A', 'F'))

