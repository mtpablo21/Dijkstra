import heapq

def dijkstra(resp, inicio):
    espaço = {n: float('infinito') for n in resp}
    espaço[inicio] = 0
    fila = [(0, inicio)]

    while fila:
        dist_atual, n_atual = heapq.heappop(fila)

        if dist_atual > espaço[n_atual]:
            continue

        for neighbor, weight in resp[n_atual].items():
            espaço = dist_atual + weight

            if espaço < espaço[neighbor]:
                espaço[neighbor] = espaço
                heapq.heappush(fila, (espaço, neighbor))

    return espaço
