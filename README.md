
# Robot Movement Simulation

This Python program simulates a robot moving on a 5x4 grid based on directional (`N`, `E`, `W`, `S`) and movement (`M`) commands.

## Grid Configuration
- **Grid Size:** 5 (width) x 4 (height)
- **Initial Position:** (0, 0)
- **Initial Direction:** South ('S')

## Movement Instructions
The robot can take two types of instructions:
1. **Directional Instructions:** `N`, `E`, `W`, `S` (North, East, West, South) - Change the direction the robot is facing.
2. **Movement Instruction:** `M` - Move one step in the direction the robot is currently facing.

## Code Overview

### Movement Vectors
- The `MOVEMENTS` dictionary defines how the robot moves in each direction:
  - `N` (North): Move up in the grid (decrease row).
  - `E` (East): Move right in the grid (increase column).
  - `S` (South): Move down in the grid (increase row).
  - `W` (West): Move left in the grid (decrease column).

### Execution Logic
- The `execute_commands` function processes a sequence of commands and returns the final position and direction of the robot.
- If a movement would take the robot out of the grid bounds, it will not move.

### Example Usage

```python
if __name__ == "__main__":
    # Example command sequence
    command_input = "MSMMEMM"

    # Execute the command and get the final position and direction
    final_position, final_direction = execute_commands(command_input)

    # Output the final position and direction
    print(f"Robot Location: {final_position + (final_direction,)}")
```

For the command sequence `MSMMEMM`, the robot ends at `(3, 3, 'E')`.

## Running the Program

1. Clone the repository or download the script.
2. Run the Python script.
3. Enter the desired command sequence to move the robot.

```bash
python robot_movement.py
```


