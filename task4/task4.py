from sys import argv

x = argv[1]
nums = []
with open(x) as file1:
    for line in file1:
        nums.append(int(line.strip('\n')))

result_digit = sorted(nums)[len(nums) // 2]
count = 0

for x, i in enumerate(nums):
    while i != result_digit:
        if i < result_digit:
            i += 1
            count += 1
        elif i > result_digit:
            i -= 1
            count += 1
        else:
            nums[x] = i
print(count)




