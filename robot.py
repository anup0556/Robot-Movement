GRID_WIDTH = 5
GRID_HEIGHT = 4


initial_position = (0, 0)  # (row, column)
initial_direction = 'S'


MOVEMENTS = {
    'N': (-1, 0),  # North: move up in the grid (decrease row)
    'E': (0, 1),   # East: move right in the grid (increase column)
    'S': (1, 0),   # South: move down in the grid (increase row)
    'W': (0, -1)   # West: move left in the grid (decrease column)
}

def execute_commands(commands):
    position = list(initial_position)
    direction = initial_direction

    for command in commands:
        if command in 'NEWS':
            if direction != command:
                direction = command
        elif command == 'M':
            new_position = [
                position[0] + MOVEMENTS[direction][0],
                position[1] + MOVEMENTS[direction][1]
            ]

            
            if 0 <= new_position[0] < GRID_HEIGHT and 0 <= new_position[1] < GRID_WIDTH:
                position = new_position

    return tuple(position), direction

if __name__ == "__main__":
    
    command_input = "MSMMEMM"

    
    final_position, final_direction = execute_commands(command_input)

    
    print(f"Robot Location: {final_position + (final_direction,)}")
