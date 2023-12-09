def prev_term(nums: list) -> int:
    if max(nums) == min(nums) == 0:
        return 0
    diffs = [nums[i+1] - nums[i] for i in range(len(nums) - 1)]
    return nums[0] - prev_term(diffs)
    

with open("in.txt") as file:
    lines = file.read().split("\n")

total = 0
for line in lines:
    nums = [int(num) for num in line.split()]
    total += prev_term(nums)

print(total)