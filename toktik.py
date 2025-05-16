ins = int(input())
followers = {}
for x in range(ins):
    data = input().split()
    name = data[0]
    count = int(data[1])
    if name in followers:
        followers[name] += count
    else:
        followers[name] = count
max_name = ""
max_followers = 0
for name, count in followers.items():
    if count > max_followers:
        max_followers = count
        max_name = name
print(max_name)
