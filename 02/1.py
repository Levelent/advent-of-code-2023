def is_game_possible(line: str, available_cubes: dict[str, int]) -> bool:
    # Possible if no game configuration needs more than the available cubes 
    configs = line.split(";")

    for config in configs:
        entries = config.split(",")

        for entry in entries:
            val, key = entry.split()
            if available_cubes[key] < int(val):
                return False
    
    return True

if __name__ == "__main__":
    available_cubes = {"red": 12, "green": 13, "blue": 14}

    num_games = int(input())

    total = 0
    for game_number in range(1, num_games + 1):
        line = input()
        
        # Strip game number
        line = line[line.find(":")+1:]

        if is_game_possible(line, available_cubes):
            total += game_number

    print(total)
