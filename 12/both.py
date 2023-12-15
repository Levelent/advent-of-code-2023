from functools import cache


# haha cache decorator go brrr
@cache
def valid_configs(pattern: str, nums: list[int], last_hash: bool) -> int:
    # Empty pattern string
    if len(pattern) == 0:
        return len(nums) == 0

    match pattern[0]:
        case "?":
            # Split into . and # cases
            num_dot = valid_configs("." + pattern[1:], nums, last_hash)
            num_hash = valid_configs("#" + pattern[1:], nums, last_hash)
            return num_dot + num_hash

        case "#":
            if len(nums) == 0:
                return 0

            # reduce current num value
            nums = tuple(tuple([nums[0] - 1]) + nums[1:])
            if nums[0] < 0:
                return 0
            return valid_configs(pattern[1:], nums, True)

        case ".":
            if last_hash:
                # check the current number is fully consumed
                if len(nums) == 0 or nums[0] != 0:
                    return 0
                nums = nums[1:]

            return valid_configs(pattern[1:], nums, False)

    raise Exception("oh dear")


with open("in.txt") as file:
    lines = file.read().split("\n")

total_p1 = 0
total_p2 = 0

for line in lines:
    pattern_p1, str_nums = line.split()
    nums = [int(num) for num in str_nums.split(",")]

    nums_p1 = tuple(nums)
    # adding ending "." avoids edge cases without changing result
    total_p1 += valid_configs(pattern_p1 + ".", nums_p1, False)

    nums_p2 = tuple(nums * 5)
    pattern_p2 = "?".join([pattern_p1] * 5)
    total_p2 += valid_configs(pattern_p2 + ".", nums_p2, False)

print("Part 1:", total_p1)
print("Part 2:", total_p2)
