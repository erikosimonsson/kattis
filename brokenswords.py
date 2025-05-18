slats = [0, 0, 0, 0]
for x in range(int(input())):
    parts = input()
    for y in range(len(parts)):
        if parts[y] == '0':
            slats[y] += 1
tb = slats[0] + slats[1]
lr = slats[2] + slats[3]
whole = 0
if tb > lr:
    if lr % 2 == 1:
        whole = (lr - 1) / 2
    else:
        whole = lr / 2
    lr -= whole * 2
    tb -= whole * 2
else:
    if tb % 2 == 1:
        whole = (tb - 1) / 2
    else:
        whole = tb / 2
    tb -= whole * 2
    lr -= whole * 2
print(int(whole), int(tb), int(lr))
