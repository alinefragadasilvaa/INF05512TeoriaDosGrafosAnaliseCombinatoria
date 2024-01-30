def push(lista_prioridade, novo):
    lista_prioridade.append(novo) # adiciona aresta no fim da lista de prioridade
    corrige_push(lista_prioridade, len(lista_prioridade) - 1) # corrige a ordenação da lista

def corrige_push(lista_prioridade, posicao):
    while posicao > 0: # modifica a posição da aresta na lista de prioridade enquanto ela for menor que seu pai na lista ou enquanto ela não for a primeira da lista
        posicao_pai = (posicao - 1) // 2  
        if lista_prioridade[posicao] < lista_prioridade[posicao_pai]: 
            lista_prioridade[posicao], lista_prioridade[posicao_pai] = lista_prioridade[posicao_pai], lista_prioridade[posicao]
            posicao = posicao_pai
        else:
            break

def pop(lista_prioridade):
    if len(lista_prioridade) == 0:
        raise IndexError("Lista de prioridade vazia...")

    removido = lista_prioridade[0] # remove a menor aresta da lista de prioridades
    
    lista_prioridade[0] = lista_prioridade[-1] # coloca a última aresta no lugar da removida
    del lista_prioridade[-1]

    corrige_pop(lista_prioridade, 0) #corrige a ordenação da lista

    return removido

def corrige_pop(lista_prioridade, posicao_removido):
    tamanho_lista = len(lista_prioridade)

    while True: # modifica a posição da aresta que substituiu a removida até que ela não seja menor que seu menor filho na lista
        posicao_filho_esq = 2 * posicao_removido + 1
        posicao_filho_dir = 2 * posicao_removido + 2

        posicao_menor_filho = posicao_filho_esq

        if posicao_filho_dir < tamanho_lista and lista_prioridade[posicao_filho_dir] < lista_prioridade[posicao_filho_esq]:
            posicao_menor_filho = posicao_filho_dir

        if posicao_menor_filho < tamanho_lista and lista_prioridade[posicao_menor_filho] < lista_prioridade[posicao_removido]:
            lista_prioridade[posicao_removido], lista_prioridade[posicao_menor_filho] = lista_prioridade[posicao_menor_filho], lista_prioridade[posicao_removido]
            posicao_removido = posicao_menor_filho
        else:
            break

def prim(grafo):
    visitados = [False] * len(grafo)
    custo_arvore = 0

    vertice = 0 # vertice inicial
    visitados[vertice] = True

    lista_prioridade = []
    
    for peso, vizinho in grafo[vertice]: # adiciona arestas que inicidem no vertice na lista de prioridade
            if (not visitados[vizinho]):
                push(lista_prioridade, (peso, vizinho))

    while lista_prioridade:
        peso, vizinho = pop(lista_prioridade)

        if (not visitados[vizinho]):
            visitados[vizinho] = True 
            custo_arvore += peso # adiciona aresta ao custo da árvore geradora mínima
        
            for peso, vizinho in grafo[vizinho]: # adiciona arestas que inicidem no vertice na lista de prioridade
                if (not visitados[vizinho]):
                    push(lista_prioridade, (peso, vizinho))

    return custo_arvore
    

def main():

    while(True):
        num_vertices, num_arestas = map(int, input().split()) # lê primeira linha

        if(num_vertices==0 and num_arestas==0): # encerra a leitura
            break

        grafo = {vertice: [] for vertice in range(num_vertices)} # lista de adjacência (peso, vizinho)
        custo_grafo = 0

        for aresta in range(num_arestas):
            verticeUm, verticeDois, peso = map(int, input().split()) # lê arestas

            grafo[verticeUm].append((peso, verticeDois)) # monta o grafo
            grafo[verticeDois].append((peso, verticeUm))

            custo_grafo += peso # atualiza custo total do grafo
        
        custo_arvore = prim(grafo)
        economia = custo_grafo - custo_arvore 
        print(economia)

if __name__ == "__main__":
    main()
