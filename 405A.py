x = int(input())

tall = list(map(int, input().split()))

tall.sort()

print(*tall)