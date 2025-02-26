# GRUPO 10
#
# Nomes: Caio Cezar Miranda Carvalho
#        Letícia de Oliveira Soares
#        Matheus Monteiro Huebra Perdigão
#


def finds_min_byteladian_dollars(m, roads, parent, rank):

    amount_byteladian = 0

    k = 0
    while k < (m-1):
        junction1, junction2, length = roads.pop()
        
        while parent[junction1] != junction1:
            junction1 = parent[junction1]

        while parent[junction2] != junction2:
            junction2 = parent[junction2]
            

        if junction1 != junction2:
            k += 1
            amount_byteladian = amount_byteladian + length

            if rank[junction1] < rank[junction2]:
                parent[junction1] = junction2
                rank[junction2] = rank[junction2] + 1
            else:
                parent[junction2] = junction1
                rank[junction1] = rank[junction1] + 1

    return amount_byteladian



def daily_amount_saved(total, m, roads, parent, rank):
    amount_saved = total - finds_min_byteladian_dollars(m=m, roads=roads, parent=parent, rank=rank)
    return amount_saved


while True:

    user_input = input()
    if user_input == '0 0':
        break

    qnt_junctions_roads = user_input.split()
    m = int(qnt_junctions_roads[0])
    n = int(qnt_junctions_roads[1])

    junctions = []
    parent = {}
    rank = {}
    roads = []
    for i in range(m):
        junctions.append(i)
        parent[i] = i
        rank[i] = 1   

    total_byteladian_dollars = 0

    for _ in range(n):
        inputizinho = input().split()
        x = int(inputizinho[0])
        y = int(inputizinho[1])
        z = int(inputizinho[2])
        roads.append((x, y, z))

        total_byteladian_dollars = total_byteladian_dollars + z

    roads.sort(key=lambda edge: edge[2], reverse=True)
    print(daily_amount_saved(total=total_byteladian_dollars, m=m, roads=roads, parent=parent, rank=rank))