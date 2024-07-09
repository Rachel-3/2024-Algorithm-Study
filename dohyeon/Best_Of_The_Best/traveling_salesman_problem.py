import itertools


def calc(distances) :
    city = len(distances)

    min_distance = float('inf')
    shortest_path = None

    for perm in itertools.permutations(range(city)):
        current_distance = sum(distances[perm[i]][perm[i + 1]] for i in range(city - 1))
        current_distance += distances[perm[-1]][perm[0]]
        
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = perm

    print("최단 경로 :", '-'.join(map(str, shortest_path)) + "-" + str(shortest_path[0]))
    print("최소 비용 :", min_distance)
    return ""

distances_1 = [
    [0, 100, 150, 200],
    [100, 0, 250, 300],
    [150, 250, 0, 350],
    [200, 300, 350, 0]
]

distances_2 = [
    [0, 120, 180, 240],
    [120, 0, 200, 300],
    [180, 200, 0, 160],
    [240, 300, 160, 0]
]

distances_3 = [
    [0, 90, 160, 230],
    [90, 0, 140, 270],
    [160, 140, 0, 210],
    [230, 270, 210, 0]
]

distances_4 = [
    [0, 80, 170, 260],
    [80, 0, 150, 280],
    [170, 150, 0, 190],
    [260, 280, 190, 0]
]

distances_5 = [
    [0, 110, 130, 220],
    [110, 0, 210, 240],
    [130, 210, 0, 180],
    [220, 240, 180, 0]
]

print(calc(distances_1))
print(calc(distances_2))
print(calc(distances_3))
print(calc(distances_4))
print(calc(distances_5))
