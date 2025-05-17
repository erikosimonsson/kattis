sum = int(input().split()[1])
nums = list(map(int, input().split()))
checked = set()
for x in range(len(nums)):
    n = nums[x]
    if (sum - n) in checked:
        print("YES")
        exit()
    rev = str(n)
    if "3" not in rev and "4" not in rev and "7" not in rev:
        flip = ""
        for char in rev[::-1]:
            if char == '6':
                flip += '9'
            elif char == '9':
                flip += '6'
            else:
                flip += char
        if (sum - int(flip)) in checked:
            print("YES")
            exit()
        checked.add(int(flip))
    checked.add(n)
print("NO")
