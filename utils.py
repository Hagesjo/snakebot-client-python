def logging_format(input_dict, depth=1, outp=""):
    for key, value in input_dict.items():
        if type(value) == dict:
            outp += logging_format(value, depth + 1)
        else:
            outp += "{}{} = {}\n".format("\t" * depth, key, value)
    return outp

def direction_as_movement_delta(direction):
    directions = {"DOWN"  : (0, 1),
            "UP"    : (0, -1),
            "RIGHT" : (1, 0),
            "LEFT"  : (-1, 0)}

    return directions[direction]

def inside_map(game_map, coordinate):
    x, y = coordinate
    return 0 <= x <= game_map.width and 0 <= y <= game_map.height

def get_snake_by_id(game_map, snake_id):
    for snake_info in game_map.snakeInfos:
        if snake_info['id'] == snake_id:
            return snake_info['name']
    else:
        return False

def get_tile_at(game_map, coordinate):
    position = translate_coordinate(game_map, coordinate)
    if position in game_map.obstaclePositions:
        return "obstacle"
    elif position in game_map.foodPositions:
        return "food"
    for snake in game_map.snakeInfos:
        if position in snake['positions']:
            tile_type = snake['positions'].index()
            if index == len(snake['positions']) - 1:
                return "snaketail"
            elif index == 0:
                return "snakebody"
            else:
                return "snakehead"
    if inside_map(game_map, coordinate):
        return "empty"
    else:
        return "wall"

def is_tile_available_for_movement(game_map, coordinate):
    tile = get_tile_at(game_map, coordinate)
    return tile in ["empty", "food", "snaketail"]


def translate_position(game_map, position):
    y = position / game_map.width
    x = abs(position - y * game_map.width)
    return x, y

def translate_positions(game_map, positions):
    return [translate_position(game_map, p) for p in positions]

def translate_coordinate(game_map, coordinate):
    x, y = coordinate
    return x + y * game_map.width

def get_manhattan_distance(start, goal):
    xs, ys = start
    xg, yg = goal

    x = abs(xs - xg)
    y = abs(ys - yg)

    return x + y

def get_euclidian_distance(start, goal):
    xs, ys = start
    xg, yg = goal

    x = (xs - xg) ** 2
    y = (ys - yg) ** 2

    return (x, y) ** 0.5

def is_within_square(coord, ne_coord, sw_coord):
    x, y = coord
    x_ne, y_ne = ne_coord
    x_sw, y_sw = sw_coord

    return x < ne_x or x > sw_x or y < sw_y or y > ne_y
