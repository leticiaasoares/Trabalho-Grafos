# GRUPO 10
#
# Nomes: Caio Cezar Miranda Carvalho
#        Letícia de Oliveira Soares
#        Matheus Monteiro Huebra Perdigão
#


class Line:
    def __init__(self, campuses):
        self.campuses = campuses

def finds_min_cost(N, lines):
    queue = []
    lines_copy = lines.copy()
    for line in lines:
        if 1 in line.campuses:
            queue.append((1, line))  #custo, linha q entrou
            lines_copy.remove(line)
    lines = lines_copy

    index = 0
    while queue:
        curr = queue[index]
        index += 1

        if N in curr[1].campuses: #se o campus estiver na linha
            return curr[0]
        
        lines_copy = lines.copy()
        for line in lines:
            if len((curr[1].campuses).intersection(line.campuses)) > 0:
                queue.append((curr[0]+1, line))
                lines_copy.remove(line)
        lines = lines_copy

    print('eroo!!!')


info = input().split()
N = int(info[0])
K = int(info[1])

lines = set()
for _ in range(K):
    line = list(map(int, input().split()))[1:]  
    lines.add(Line(set(line)))

cost = finds_min_cost(N, lines)
print(cost)