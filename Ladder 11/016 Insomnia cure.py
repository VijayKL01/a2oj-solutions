a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

count = e

for i in range(e, -1, -1):
    if ((i % a != 0) and (i % b != 0) and (i % c != 0) and (i % d != 0)):
        count -= 1

print(count)
