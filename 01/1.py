total = 0
for _ in range(1000):
    line = input()
    # ASCII codepoints 48 to 57 are the digits 0 to 9
    nums = [int(char) for char in line if 48 <= ord(char) <= 57]
    total += nums[0] * 10 + nums[-1]

print(total)