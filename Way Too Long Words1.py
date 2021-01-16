n =int(input())
for i in range(n):
    name = input()
    if len(name) <= 10:
        print(name)
    else:
        print(name[0] + str(len(name[1:-1])) + name[-1])
