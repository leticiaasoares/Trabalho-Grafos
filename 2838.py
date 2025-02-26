# GRUPO 10
#
# Nomes: Caio Cezar Miranda Carvalho
#        Letícia de Oliveira Soares
#        Matheus Monteiro Huebra Perdigão
#


def try_to_get_gems(n, m, labyrinth):
    thanos_movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    all_gems = 0
    gem_bit = {'p': 1, 't': 2, 'm': 4, 'e': 8, 'r': 16}
    key_bit = {'a': 1, 'b': 2, 'c': 4, 'd': 8}

    queue = []
    
    start_pos = None
    for i in range(n):
        for j in range(m):
            char = labyrinth[i][j]
            if char == 'T':
                start_pos = (i, j)
            elif char in gem_bit:
                all_gems |= gem_bit[char]

    queue.append((start_pos[0], start_pos[1], 0, 0, 0)) 
    visited = set([(start_pos[0], start_pos[1], 0, 0)])

    index = 0
    while queue:

        if index >= len(queue):
            return None

        x, y, steps, keys, gems = queue[index]
        index += 1

        if gems == all_gems:
            return steps
        
        for dx, dy in thanos_movements:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                char = labyrinth[nx][ny]
                
                if char == '#':
                    continue

                new_keys = keys
                if char in key_bit:
                    new_keys |= key_bit[char]
                
                if char in "ABCD" and not (keys & key_bit[char.lower()]):
                    continue  
                
                new_gems = gems
                if char in gem_bit:
                    new_gems |= gem_bit[char]

                state = (nx, ny, new_keys, new_gems)
                if state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, steps + 1, new_keys, new_gems))


dimensions = input().split()
N = int(dimensions[0])
M = int(dimensions[1])

labyrinth = []
for _ in range(N):
    labyrinth.append(input())

time = try_to_get_gems(n=N, m=M, labyrinth=labyrinth)

if time is not None:
    print(time)
else:
    print('Gamora')