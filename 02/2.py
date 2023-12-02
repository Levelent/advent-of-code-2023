import math

def game_power(line: str) -> int:
    # minimum cubes required to play the game
    required_cubes = {"red": 0, "green": 0, "blue": 0}

    # don't need to consider each game config separately
    entries = line.replace(";", ",").split(",")

    for entry in entries:
        val, key = entry.split()
        val = int(val)

        if required_cubes[key] < val:
            required_cubes[key] = val
    
    # power is product of required cubes
    return math.prod(required_cubes.values())

if __name__ == "__main__":
    num_games = int(input())

    total = 0
    for _ in range(num_games):
        line = input()
        
        # Strip game number
        line = line[line.find(":")+1:]

        total += game_power(line)

    print(total)
