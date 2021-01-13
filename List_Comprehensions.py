x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = []
list = []
for i in range (x+1):
    for j in range (y+1):
        for k in range (z+1):
            if (i+j+k)!= n:
                list = [i,j,k]
                result.append(list)
print(result)
