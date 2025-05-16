roof = int(input())
combos = 0
for x in range(1, 10**9):
    if x*(x+1)*(x+2) < roof:
        combos+=1
    else:
        break
print(combos)