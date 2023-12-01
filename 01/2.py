digit_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0
for _ in range(1000):
    line = input()

    for digit, name in enumerate(digit_names):
        while (idx := line.find(name)) != -1:
            
            # keep start and end characters of digit name (for further matching)
            begin = line[:idx+1]
            end = line[idx+len(name)-1:]

            line = begin + str(digit) + end

    # ASCII codepoints 48 to 57 are the digits 0 to 9
    nums = [int(char) for char in line if 48 <= ord(char) <= 57]
    total += nums[0] * 10 + nums[-1]

print(total)