def main():
    wire_input = get_input()

    points_along_wire_one = build_wire_path(wire_input[0])
    point_alone_wire_two = build_wire_path(wire_input[1])

    intersections = get_intersections(points_along_wire_one, point_alone_wire_two)

    shortest_mann_distance = get_shortest_mann_distance(intersections)

    wire_one_distances = get_intersection_distance(intersections, points_along_wire_one)
    wire_two_distances = get_intersection_distance(intersections, point_alone_wire_two)

    print(wire_one_distances)
    print(wire_two_distances)
    print("=========")

    fewest_combined_steps = -1

    for i in range(len(wire_one_distances)):
        combined_steps = wire_one_distances[i] + wire_two_distances[i]
        if i == 0 or fewest_combined_steps > combined_steps:
            fewest_combined_steps = combined_steps + 2

    print(shortest_mann_distance)

    print("============")

    print(fewest_combined_steps)



def get_input():
    file = open("input.txt", 'r', encoding="utf-8")
    return [line.rstrip() for line in file]

def build_wire_path(wireInputStr):
    path = []
    current_point = (0, 0)
    for instruction in wireInputStr.split(','):
        direction = instruction[0]
        for i in range(int(instruction[1:])):
            if direction == 'L':
                new_point = (current_point[0] - 1, current_point[1])
            elif direction == 'R':
                new_point = (current_point[0] + 1, current_point[1])
            elif direction == 'D':
                new_point = (current_point[0], current_point[1] - 1)
            else:
                new_point = (current_point[0], current_point[1] + 1)

            path.append(new_point)
            current_point = new_point

    return path

def get_intersections(points_one, points_two):
    return list(set(points_one).intersection(set(points_two)))

def get_shortest_mann_distance(intersections):
    shortest_mann_distance = -1

    for item in intersections:
        item_distance = calc_manhattan_difference(item)
        if shortest_mann_distance == -1 or item_distance < shortest_mann_distance:
            shortest_mann_distance = item_distance

    return shortest_mann_distance

def get_intersection_distance(intersections, points_list):
    distances = []
    for point in intersections:
        try:
            distance_to_point = points_list.index(point)
            distances.append(distance_to_point)
        except ValueError:
            continue
    return distances

def calc_manhattan_difference(point):
    diff = abs(int(point[0])) + abs(int(point[1]))
    return diff

def calc_shortest_path():
    return -99

if __name__ == "__main__":
    main()