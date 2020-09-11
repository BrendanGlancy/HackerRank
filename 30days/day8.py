# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
d = dict()

for i in range(0, n):
    name, number = input().split()
    d[name] = number

for i in range(0, n):
    try:
        name = input()
        if name in d:
            print(f"{name}={d[name]}")
        else:
            print("Not found")
    except:
        break
